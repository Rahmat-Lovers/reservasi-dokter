<script>
    import Navbar from "../components/Navbar.svelte";
    import cookie from "cookie";
    import axios from "axios";

    const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

    let token;
    let query = "";
    let doctors = [];

    (async () => {
        token = cookie.parse(document.cookie).login;

        const responseDoctor = await axios.get(API_BASE_URL + "/doctors", {
            headers: {
                Authorization: "Bearer " + token,
            },
        });
        doctors = responseDoctor.data.data;
    })();
</script>

<div>
    <div class="main px-0 bg-white">
        <div class="bg-[#1363DF] h-16 flex items-center p-3">
            <div
                class="flex items-center bg-[#F3F3F3] w-full h-10 rounded-lg px-3"
            >
                <div>
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke-width="1.5"
                        stroke="currentColor"
                        class="w-6 h-6"
                    >
                        <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"
                        />
                    </svg>
                </div>
                <div class="ml-2 w-full">
                    <input
                        type="text"
                        class="w-full bg-transparent outline-none"
                        bind:value={query}
                        on:change={async () => {
                            token = cookie.parse(document.cookie).login;

                            const responseDoctor = await axios.get(
                                API_BASE_URL + "/doctors",
                                {
                                    headers: {
                                        Authorization: "Bearer " + token,
                                    },
                                    params: {
                                        query
                                    }
                                }
                            )
                            doctors = responseDoctor.data.data;
                        }}
                    />
                </div>
            </div>
        </div>

        <div class=" flex flex-col gap-1 h-[800px] mt-2 px-3">
            {#each doctors as doctor}
                <div
                    class=" flex items-center justify-between mx-auto h-16 w-full bg-slate-100 rounded"
                >
                    <div class=" w-10 h-10 mx-4 bg-[#3DB2FF] rounded-full">
                        <img src="" alt="" />
                    </div>
                    <div class=" w-40 h-10 -ml-14">
                        <p
                            class=" text-sm tracking-wide text-[#5A5A5A] font-semibold"
                        >
                            Dr. {doctor.customer.name}
                        </p>
                        <p class=" text-[10px] tracking-wide text-[#5A5A5A]">
                            Spesialis {doctor.specialist
                                .map((x) => x.name)
                                .join(", ")}
                        </p>
                    </div>
                    <div
                        class=" w-5 h-5 mr-2 bg-transparent opacity-40 rounded-md"
                    >
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
            {/each}
        </div>
    </div>
    <Navbar />
</div>
