import { useEffect, useRef, useState } from "react";

/** 마우스를 따라 별이 생겼다가 떠오르며 사라지는 오버레이 */
export default function CursorStars({ color = "rgb(90 80 160)", density = 1 }) {
    const [stars, setStars] = useState([]);
    const lastRef = useRef(0);

useEffect(() => {
    const addStars = (x, y) => {
        const now = performance.now();
        if (now - lastRef.current < 60) return; // 스로틀 간격 증가로 생성 빈도 감소
            lastRef.current = now;

        const created = Array.from({ length: density }, () => {
            const id = crypto.randomUUID();
            return {
                id,
                x, y,
                size: 6 + Math.random() * 10, // 가시성 유지
                dx: (Math.random() - 0.5) * 20,
                dy: -10 - Math.random() * 20,
                rot: (Math.random() * 60 - 30),
                dur: 2400 + Math.random() * 2000
            };
        });

        setStars(prev => {
            const next = [...prev, ...created];
            return next.length > 120 ? next.slice(next.length - 120) : next;
        });

        created.forEach(s => {
            setTimeout(() => {
                setStars(prev => prev.filter(p => p.id !== s.id));
            }, s.dur);
        });
    };

    const onMove = e => addStars(e.clientX, e.clientY);
    window.addEventListener("pointermove", onMove, { passive: true });
    return () => window.removeEventListener("pointermove", onMove);
    }, [density]);

    return (
    <div className="pointer-events-none fixed inset-0 overflow-hidden z-50" aria-hidden>
        {stars.map(s => (
        <svg
            key={s.id}
            className="cursor-star"
            viewBox="0 0 24 24"
            style={{
            left: s.x, top: s.y, width: s.size, height: s.size,
            color,
            "--tx": `${s.dx}px`,
            "--ty": `${s.dy}px`,
            "--rot": `${s.rot}deg`,
            "--dur": `${s.dur}ms`,
            }}
        >
            <polygon
            fill="currentColor"
            points="12,2 15.09,8.26 22,9.27 17,13.97 18.18,21 12,17.77 5.82,21 7,13.97 2,9.27 8.91,8.26"
            />
        </svg>
        ))}
    </div>
    );
}