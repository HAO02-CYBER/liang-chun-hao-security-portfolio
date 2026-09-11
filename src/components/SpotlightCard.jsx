import React, { useRef } from "react";

export default function SpotlightCard({
  children,
  className = "",
  spotlightColor = "rgba(129, 246, 210, 0.18)",
  ...props
}) {
  const cardRef = useRef(null);

  const handlePointerMove = (event) => {
    const bounds = cardRef.current?.getBoundingClientRect();
    if (!bounds) return;
    cardRef.current.style.setProperty("--mouse-x", `${event.clientX - bounds.left}px`);
    cardRef.current.style.setProperty("--mouse-y", `${event.clientY - bounds.top}px`);
  };

  return (
    <div
      ref={cardRef}
      className={`spotlightCard ${className}`}
      style={{ "--spotlight-color": spotlightColor }}
      onPointerMove={handlePointerMove}
      {...props}
    >
      {children}
    </div>
  );
}
