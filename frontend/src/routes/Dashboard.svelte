<script>
    import Loading from "../components/Loading.svelte";
    import axios from "axios";
    import cookie, { parse } from "cookie";
    import { getDistanceYear } from "../helpers";

    const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

    let loading = true;
    let token;
    let data;
    let doctors = [];

    (async () => {
        token = cookie.parse(document.cookie).login;
        const response = await axios.get(API_BASE_URL + "/me", {
            headers: {
                Authorization: "Bearer " + token,
            },
        });
        data = response.data.data;

        const responseDoctor = await axios.get(API_BASE_URL + "/doctors", {
            headers: {
                Authorization: "Bearer " + token,
            },
        });
        doctors = responseDoctor.data.data;

        loading = false;
    })();
</script>

<Loading bind:isLoading={loading} />

<div>
    <!-- ========================================       HEADER      ========================================== -->
    <div
        class=" h-12 w-[360px] mx-auto bg-[#1363DF] flex justify-around items-center"
    >
        <div class=" relative h-7 w-64 mx-auto bg-slate-100 rounded-3xl">
            <input
                type="text"
                class=" w-full h-full rounded-lg relative pl-8 outline-none"
            />
            <span class="inline-block absolute top-0 left-2"
                ><img
                    src="/img/search.png"
                    alt="icon search bar"
                    class=" w-6 h-6 inline-block"
                /></span
            >
        </div>
        <div class=" w-8 h-8 mx-auto rounded-lg">
            <img
                src="/img/notification.png"
                alt="icon notification"
                class=" w-6 h-6 mt-1 mx-auto"
            />
        </div>
    </div>

    <!-- ========================================     CARD INFO      ========================================== -->
    <div
        class=" h-32 my-4 w-[330px] mx-auto bg-[#3DB2FF] rounded-lg overflow-hidden"
    >
        <div class=" flex items-center h-16 w-80">
            <div class=" w-10 h-10 mx-4 bg-white rounded-full" />
            <div class=" w-40 h-10">
                <p class=" text-md tracking-wide text-white font-semibold">
                    Dr. Soihib al-sohib
                </p>
                <p class=" text-[10px] tracking-wide text-white">
                    Ahli kesehatan jasmani
                </p>
            </div>
        </div>
        <div
            class="flex items-center w-72 h-10 mx-auto mt-1 bg-[#DAF0FF] rounded-lg text-[10px]"
        >
            <span class=" ml-3 inline-block w-5 h-5 rounded-md"
                ><img src="/img/calendar.png" alt="icon calender" /></span
            >
            <span class=" ml-2 text-black tracking-wide"
                >Minggu, 00 - bulan - 0000</span
            >
            <span class=" ml-3 inline-block w-5 h-5 rounded-md"
                ><img src="/img/clock.png" alt="icon clock" /></span
            >
            <span class=" ml-2 text-black tracking-normal"
                >00:00 - 00:00 wib</span
            >
        </div>
    </div>

    <!-- =======================================       SERVICE       ========================================= -->
    <div class=" h-24 w-[360px] my-2 mx-auto bg-slate-50">
        <p class=" mt-2 ml-3 mb-2 text-sm font-semibold tracking-wide">
            Layanan
        </p>
        <div class="flex justify-around items-center w-full h-16">
            <div class=" w-20 h-16 mx-5">
                <div class=" w-12 h-12 mx-auto bg-[#AFE5FF] rounded-full">
                    <div
                        class=" w-9 h-9 translate-y-[6px] mx-auto bg-[#3DB2FF] rounded-full"
                    />
                </div>
                <div class=" text-center text-xs text-black font-medium">
                    Layanan 1
                </div>
            </div>

            <div class=" w-20 h-16 mx-5">
                <div class=" w-12 h-12 mx-auto bg-[#AFE5FF] rounded-full">
                    <div
                        class=" w-9 h-9 translate-y-[6px] mx-auto bg-[#3DB2FF] rounded-full"
                    />
                </div>
                <div class=" text-center text-xs text-black font-medium">
                    Layanan 2
                </div>
            </div>

            <div class=" w-20 h-16 mx-5">
                <div class=" w-12 h-12 mx-auto bg-[#AFE5FF] rounded-full">
                    <div
                        class=" w-9 h-9 translate-y-[6px] mx-auto bg-[#3DB2FF] rounded-full"
                    />
                </div>
                <div class=" text-center text-xs text-black font-medium">
                    Layanan 3
                </div>
            </div>
        </div>
    </div>

    <!-- =======================================       STATUS        ========================================= -->
    <div class=" w-[360px] h-24 relative my-3 mx-auto bg-slate-50">
        <p class=" mt-2 ml-3 mb-0 text-sm font-semibold tracking-normal">
            Pilih Dokter
        </p>

        <div class="absolute top-7 -left-4 w-20 h-16 ml-3 z-10 bg-slate-50">
            <div
                class=" w-9 h-9 text-center text-5xl leading-6 font-semibold translate-y-[6px] mx-auto bg-slate-200 rounded-full"
            >
                +
            </div>
        </div>

        <div
            class="flex gap-2 items-center overflow-auto w-full h-18 mt-2 ml-0 mr-5 relative"
        >
            <div class=" w-20 h-16 ml-20">
                <div
                    class=" w-9 h-9 translate-y-[6px] mx-auto bg-slate-400 rounded-full"
                />
            </div>

            <div class=" w-20 h-16 ml-1">
                <div
                    class=" w-9 h-9 translate-y-[6px] mx-auto bg-slate-400 rounded-full"
                />
            </div>

            <div class=" w-20 h-16 ml-1">
                <div
                    class=" w-9 h-9 translate-y-[6px] mx-auto bg-slate-400 rounded-full"
                />
            </div>

            <div class=" w-20 h-16 ml-1">
                <div
                    class=" w-9 h-9 translate-y-[6px] mx-auto bg-slate-400 rounded-full"
                />
            </div>

            <div class=" w-20 h-16 ml-1">
                <div
                    class=" w-9 h-9 translate-y-[6px] mx-auto bg-slate-400 rounded-full"
                />
            </div>
            <div class=" w-20 h-16 ml-1">
                <div
                    class=" w-9 h-9 translate-y-[6px] mx-auto bg-slate-400 rounded-full"
                />
            </div>
            <div class=" w-20 h-16 ml-1">
                <div
                    class=" w-9 h-9 translate-y-[6px] mx-auto bg-slate-400 rounded-full"
                />
            </div>
        </div>
    </div>

    <!-- =======================================     CARD DOCTORS    ========================================= -->
    <div class=" w-[360px] h-36 my-2 mx-auto bg-slate-100">
        <p class="mt-2 ml-3 text-sm font-semibold tracking-normal">
            Rekomedasi Dokter
        </p>
        <div
            class="grid grid-cols-2 gap-2 overflow-auto px-2 w-full h-32 bg-slate-100 mb-2"
        >
            {#each doctors as doctor}
                <div class=" h-28 bg-[#3DB2FF] rounded-xl">
                    <div class=" mt-2 ml-2 w-8 h-8 bg-white rounded-full" />
                    <div class=" w-full h-auto mt-2 px-2">
                        <p class=" text-white text-[9px]">
                            Dr. {doctor.customer.name}
                        </p>
                        <p class=" text-white text-[8px] tracking-wide">
                            Spesialis {doctor.specialist
                                .map((x) => x.name)
                                .join(", ")}
                        </p>
                    </div>
                    {#if doctor.followed}
                        <button
                            class="text-white block w-16 h-5 translate-y-2 mx-auto text-[10px] leading-5 text-center font-semibold bg-gray-400 rounded-md"
                            on:click={async () => {
                                const response = await axios.delete(
                                    API_BASE_URL + "/follow/" + doctor.id,
                                    {
                                        headers: {
                                            Authorization: "Bearer " + token,
                                        },
                                    }
                                );
                                doctor.followed = false;
                            }}>Followed</button
                        >
                    {:else}
                        <button
                            class="block w-16 h-5 translate-y-2 mx-auto text-[10px] leading-5 text-center font-semibold bg-white rounded-md"
                            on:click={async () => {
                                const response = await axios.post(
                                    API_BASE_URL + "/follow/" + doctor.id,
                                    {},
                                    {
                                        headers: {
                                            Authorization: "Bearer " + token,
                                        },
                                    }
                                );
                                doctor.followed = true;
                            }}
                        >
                            Follow
                        </button>
                    {/if}
                </div>
            {/each}
        </div>
    </div>

    <!-- ======================================     NAVIGATION BAR    ======================================== -->
    <div
        class=" w-[360px] h-12 fixed bottom-0 left-[50%] -translate-x-1/2 flex justify-around items-center flex-wrap mx-auto font-semibold bg-slate-50 shadow-sm shadow-gray-500"
    >
        <div class="relative w-10 h-auto">
            <div
                class=" w-6 h-6 top-0 left-0 translate-x-2 bg-slate-400 rounded-full"
            />
            <span class=" block w-7 h-auto mx-auto text-[8px] tracking-wide"
                >Beranda</span
            >
        </div>

        <div class="relative w-auto h-auto text-center">
            <div
                class=" w-6 h-6 top-0 left-0 translate-x-2 bg-slate-400 rounded-full"
            />
            <span class=" block w-auto h-auto mx-auto text-[8px] tracking-wide"
                >Cari Dokter</span
            >
        </div>

        <div class="relative w-10 h-auto text-center">
            <div
                class=" w-6 h-6 top-0 left-0 translate-x-2 bg-slate-400 rounded-full"
            />
            <span class=" block w-7 h-auto mx-auto text-[8px] tracking-wide"
                >Riwayat</span
            >
        </div>

        <div class="relative w-10 h-auto text-center">
            <div
                class=" w-6 h-6 top-0 left-0 translate-x-2 bg-slate-400 rounded-full"
            />
            <span class=" block w-7 h-auto mx-auto text-[8px] tracking-wide"
                >Akun</span
            >
        </div>
    </div>

    <!-- 
    <div class=" w-[360px] h-14 fixed bottom-0 left-0 flex justify-around items-center flex-wrap mx-auto bg-blue-500 ">
        <div class=" w-6 h-6 bg-slate-100 rounded-full"></div>
        <div class=" w-6 h-6 bg-slate-100 rounded-full"></div>
        <div class=" w-6 h-6 bg-slate-100 rounded-full"></div>
        <div class=" w-6 h-6 bg-slate-100 rounded-full"></div>
    </div> -->

    <!-- AFE5FF -->
</div>
