import { useEffect, useMemo, useState } from 'react'

/**
 * segments: Array<{ text: string, className?: string }>
 * startDelay: delay before typing starts (ms)
 * speedMs: ms per character
 * caret: show blinking caret while typing
 */
export default function SegmentedTypewriter({ segments = [], startDelay = 0, speedMs = 40, caret = true }) {
    // Flatten lengths for stable stepping across segments
    const lengths = useMemo(() => segments.map(s => (s?.text ?? '').length), [segments])
    const totalChars = useMemo(() => lengths.reduce((a, b) => a + b, 0), [lengths])

    const [globalIdx, setGlobalIdx] = useState(0) // total characters revealed so far

    useEffect(() => {
        let mounted = true
        let tId
        let iId

        setGlobalIdx(0) // restart when segments change

        tId = setTimeout(() => {
            iId = setInterval(() => {
                if (!mounted) return
                setGlobalIdx(prev => {
                    if (prev >= totalChars) {
                        clearInterval(iId)
                        return prev
                    }
                    return prev + 1
                })
            }, speedMs)
        }, startDelay)

        return () => {
            mounted = false
            clearTimeout(tId)
            clearInterval(iId)
        }
    }, [startDelay, speedMs, totalChars, lengths])

    // Compute how much of each segment to show
    const parts = []
    let remaining = globalIdx
    for (let i = 0; i < segments.length; i++) {
        const seg = segments[i]
        const len = lengths[i]
        const take = Math.max(0, Math.min(len, remaining))
        const text = (seg?.text ?? '').slice(0, take)
        parts.push({ className: seg?.className, text })
        remaining -= take
        if (remaining <= 0) break
    }

    const isTyping = globalIdx < totalChars

    return (
        <span className={caret && isTyping ? 'type-caret' : ''}>
            {parts.map((seg, i) => (
                <span key={i} className={seg.className}>
                    {seg.text.split('\n').map((chunk, ci) => ci === 0 ? chunk : <span key={ci}><br />{chunk}</span>)}
                </span>
            ))}
        </span>
    )
}
