<script>
    import Navbar from "../components/Navbar.svelte"
</script>

<!-- ========================================       HEADER      ========================================== -->
<div
    class="fixed top-0 left-1/2 -translate-x-1/2 h-12 w-[360px] mx-auto bg-[#1363DF] flex justify-around items-center z-50"
>
    <div class="relative h-7 w-72 mx-auto bg-slate-100 rounded-2xl">
        <input
            type="text"
            class="relative w-full h-full pl-8 rounded-lg outline-none text-xs"
        />
        <span class=" absolute w-5 h-5 top-1 left-2 z-10"
            ><img
                src="/img/search.png"
                alt="icon search"
                class=" w-5 h-5"
            /></span
        >
    </div>
    <!-- <div class=" w-7 h-7 mx-auto -ml-2 rounded-md bg-slate-100">
        <img
            src="/img/filter.png"
            alt="icon filter"
            class=" w-4 h-4 mx-auto mt-1.5"
        />
    </div> -->
</div>

<!-- ========================================     CARD INFO      ========================================== -->
<div class=" flex flex-col gap-1 h-[800px] mt-16 w-[330px] mx-auto bg-white">
    <div
        class=" flex items-center justify-between mx-auto h-16 w-full bg-slate-100 rounded"
    >
        <div class=" w-10 h-10 mx-4 bg-[#3DB2FF] rounded-full">
            <img src="" alt="" />
        </div>
        <div class=" w-40 h-10 -ml-14">
            <p class=" text-sm tracking-wide text-[#5A5A5A] font-semibold">
                Dr. Soihib al-sohib
            </p>
            <p class=" text-[10px] tracking-wide text-[#5A5A5A]">
                Ahli kesehatan jasmani
            </p>
        </div>
        <div class=" w-5 h-5 mr-2 bg-transparent opacity-40 rounded-md">
            <i>
                <svg
                    aria-hidden="true"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="1.6"
                    viewBox="0 0 24 24"
                    xmlns="http://www.w3.org/2000/svg"
                >
                    <path
                        d="M8.25 4.5l7.5 7.5-7.5 7.5"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                    />
                </svg>
            </i>
        </div>
    </div>

    <div
        class=" flex items-center justify-between mx-auto h-16 w-full bg-slate-100 rounded"
    >
        <div class=" w-10 h-10 mx-4 bg-[#3DB2FF] rounded-full">
            <img src="" alt="" />
        </div>
        <div class=" w-40 h-10 -ml-14">
            <p class=" text-sm tracking-wide text-[#5A5A5A] font-semibold">
                Dr. Soihib al-sohib
            </p>
            <p class=" text-[10px] tracking-wide text-[#5A5A5A]">
                Ahli kesehatan jasmani
            </p>
        </div>
        <div class=" w-5 h-5 mr-2 bg-transparent opacity-40 rounded-md">
            <i>
                <svg
                    aria-hidden="true"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="1.6"
                    viewBox="0 0 24 24"
                    xmlns="http://www.w3.org/2000/svg"
                >
                    <path
                        d="M8.25 4.5l7.5 7.5-7.5 7.5"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                    />
                </svg>
            </i>
        </div>
    </div>
</div>

<!-- ======================================       NAVIGATION      ======================================== -->
<Navbar />
