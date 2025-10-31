import { useEffect, useState } from 'react'

export default function Typewriter({ text = '', startDelay = 0, speedMs = 40, className = '', caret = true }) {
    const [displayLen, setDisplayLen] = useState(0)

    useEffect(() => {
        let mounted = true
        let timeoutId
        let intervalId

        timeoutId = setTimeout(() => {
            intervalId = setInterval(() => {
                if (!mounted) return
                setDisplayLen(prev => {
                    if (prev >= text.length) {
                        clearInterval(intervalId)
                        return prev
                    }
                    return prev + 1
                })
            }, speedMs)
        }, startDelay)

        return () => {
            mounted = false
            clearTimeout(timeoutId)
            clearInterval(intervalId)
        }
    }, [text, startDelay, speedMs])

    const visible = text.slice(0, displayLen)

    return (
        <span className={caret && displayLen < text.length ? `${className} type-caret` : className}>
            {visible.split('\n').map((chunk, idx) => (
                idx === 0 ? chunk : <span key={idx}><br />{chunk}</span>
            ))}
        </span>
    )
}
