import React, { useEffect, useRef, useState } from "react";

const scrambleCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

function useInViewOnce() {
  const ref = useRef(null);
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const node = ref.current;
    if (!node || window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      setVisible(true);
      return undefined;
    }

    const observer = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting) {
        setVisible(true);
        observer.disconnect();
      }
    }, { threshold: 0.16 });

    observer.observe(node);
    return () => observer.disconnect();
  }, []);

  return [ref, visible];
}

export function RevealText({ as: Tag = "p", children, className = "", variant = "paragraph" }) {
  const [ref, visible] = useInViewOnce();
  const text = String(children);
  const tokens = text.split(/(\s+)/);

  return (
    <Tag ref={ref} className={`animatedText textReveal textReveal--${variant} ${visible ? "isVisible" : ""} ${className}`} aria-label={text}>
      <span aria-hidden="true">
        {tokens.map((token, index) => (/\s/.test(token) ? token : <span className="textRevealWord" style={{ "--word-index": index }} key={`${token}-${index}`}>{token}</span>))}
      </span>
    </Tag>
  );
}

export function DecryptedText({ as: Tag = "span", children, className = "" }) {
  const text = React.Children.toArray(children).join("");
  const [displayText, setDisplayText] = useState(text);
  const timerRef = useRef(null);

  useEffect(() => () => window.clearInterval(timerRef.current), []);

  const decrypt = () => {
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches || timerRef.current) return;

    let step = 0;
    const totalSteps = Math.max(7, Math.min(15, text.length));
    timerRef.current = window.setInterval(() => {
      step += 1;
      const revealed = Math.floor((step / totalSteps) * text.length);
      setDisplayText(text.split("").map((character, index) => {
        if (character === " " || index < revealed) return character;
        return scrambleCharacters[(index * 11 + step * 7) % scrambleCharacters.length];
      }).join(""));

      if (step >= totalSteps) {
        window.clearInterval(timerRef.current);
        timerRef.current = null;
        setDisplayText(text);
      }
    }, 34);
  };

  return <Tag className={`animatedText textDecrypt ${className}`} onMouseEnter={decrypt} onFocus={decrypt} aria-label={text}>{displayText}</Tag>;
}
