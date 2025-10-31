import React from 'react'
import Typewriter from '../components/Typewriter.jsx'
import SegmentedTypewriter from '../components/SegmentedTypewriter.jsx'
import { Link } from 'react-router-dom'

function Landing() {
    return (
        <main className="min-h-screen flex flex-col justify-between items-start px-8 sm:px-14 py-10">
            <section className="max-w-5xl">
                <div className="font-nanummyeongjo tracking-16p space-y-10 text-[#9590C0] font-semibold text-[32px] sm:text-[36px] leading-relaxed">
                    <p>
                        <span className="text-[40px] font-bold mr-4 text-[#59538F]">시</span>
                        <Typewriter
                            text={'한 줄✑을 책갈피에 살짝 끼워두고,\n숨을 고릅니다.'}
                            startDelay={100}
                            speedMs={40}
                        />
                    </p>
                    <p>
                        <SegmentedTypewriter
                            startDelay={1600}
                            speedMs={40}
                            segments={[
                                { text: '바람은 ' },
                                { text: '옷', className: 'text-[40px] font-bold text-[#59538F]' },
                                { text: '깃을 살며시 스쳐가고,' }
                            ]}
                        />
                        <br />
                        <Typewriter
                            text={'밤☽은 조용히 흘러갑니다.'}
                            startDelay={2800}
                            speedMs={40}
                        />
                    </p>
                    <p>
                        <Typewriter
                            text={'말하지 않은 마음이'}
                            startDelay={3600}
                            speedMs={40}
                        />
                        <br />
                        <Typewriter
                            text={'✽고요 속에 자리를 잡습니다.'}
                            startDelay={4200}
                            speedMs={40}
                        />
                    </p>
                </div>
            </section>

            <Link to="/app" className="self-start text-left tracking-16p text-[#59538F] text-xl sm:text-2xl font-nanummyeongjo font-bold cursor-pointer">
                - 시옷 사용하기 
            </Link>
        </main>
    )
}

export default Landing
