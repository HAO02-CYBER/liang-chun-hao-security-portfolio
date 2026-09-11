import React, { useCallback, useEffect, useRef } from "react";

export default function ClickSpark({
  sparkColor = "#c7d535",
  sparkSize = 9,
  sparkRadius = 24,
  sparkCount = 8,
  duration = 420,
}) {
  const canvasRef = useRef(null);
  const sparksRef = useRef([]);
  const frameRef = useRef(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return undefined;

    const resize = () => {
      const scale = Math.min(window.devicePixelRatio || 1, 2);
      canvas.width = Math.ceil(window.innerWidth * scale);
      canvas.height = Math.ceil(window.innerHeight * scale);
      canvas.style.width = `${window.innerWidth}px`;
      canvas.style.height = `${window.innerHeight}px`;
      canvas.getContext("2d")?.setTransform(scale, 0, 0, scale, 0, 0);
    };

    resize();
    window.addEventListener("resize", resize);
    return () => window.removeEventListener("resize", resize);
  }, []);

  const paint = useCallback((timestamp) => {
    const canvas = canvasRef.current;
    const context = canvas?.getContext("2d");
    if (!canvas || !context) return;

    const scale = Math.min(window.devicePixelRatio || 1, 2);
    context.clearRect(0, 0, canvas.width / scale, canvas.height / scale);
    sparksRef.current = sparksRef.current.filter((spark) => {
      const progress = (timestamp - spark.startedAt) / duration;
      if (progress >= 1) return false;

      const eased = 1 - (1 - progress) ** 2;
      const distance = eased * sparkRadius * spark.distanceScale;
      const length = sparkSize * (1 - eased * 0.7);
      const startX = spark.x + Math.cos(spark.angle) * distance;
      const startY = spark.y + Math.sin(spark.angle) * distance;
      const endX = spark.x + Math.cos(spark.angle) * (distance + length);
      const endY = spark.y + Math.sin(spark.angle) * (distance + length);

      context.strokeStyle = sparkColor;
      context.globalAlpha = 1 - progress;
      context.lineWidth = 1.7;
      context.lineCap = "round";
      context.beginPath();
      context.moveTo(startX, startY);
      context.lineTo(endX, endY);
      context.stroke();
      return true;
    });
    context.globalAlpha = 1;
    frameRef.current = sparksRef.current.length ? window.requestAnimationFrame(paint) : null;
  }, [duration, sparkColor, sparkRadius, sparkSize]);

  useEffect(() => {
    const createSparks = (event) => {
      if (event.button !== 0 || event.detail === 0 || window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
      const startedAt = performance.now();
      sparksRef.current.push(...Array.from({ length: sparkCount }, (_, index) => ({
        x: event.clientX,
        y: event.clientY,
        startedAt,
        angle: (Math.PI * 2 * index) / sparkCount + Math.random() * 0.16,
        distanceScale: 0.85 + Math.random() * 0.3,
      })));
      if (!frameRef.current) frameRef.current = window.requestAnimationFrame(paint);
    };

    window.addEventListener("click", createSparks, { passive: true });
    return () => window.removeEventListener("click", createSparks);
  }, [paint, sparkCount]);

  useEffect(() => () => window.cancelAnimationFrame(frameRef.current), []);

  return <canvas className="global-click-spark" ref={canvasRef} aria-hidden="true" />;
}
