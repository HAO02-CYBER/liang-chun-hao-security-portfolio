import { useEffect } from "react";

export default function Particles() {
  useEffect(() => {
    let frameId;
    let pending = false;

    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return undefined;

    const move = (event) => {
      if (pending) return;
      pending = true;
      frameId = requestAnimationFrame(() => {
        const root = document.documentElement.style;
        root.setProperty("--particle-x", `${(event.clientX / window.innerWidth) * 100}%`);
        root.setProperty("--particle-y", `${(event.clientY / window.innerHeight) * 100}%`);
        pending = false;
      });
    };

    window.addEventListener("mousemove", move);
    return () => {
      window.removeEventListener("mousemove", move);
      cancelAnimationFrame(frameId);
    };
  }, []);

  return null;
}
