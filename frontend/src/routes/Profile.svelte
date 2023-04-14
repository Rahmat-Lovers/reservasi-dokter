<script>
    import Navbar from "../components/Navbar.svelte";
</script>

<div>
    <div class="main bg-white">
        <div>
            <div class="bg-[#1363DF] pt-2 text-white pb-12 rounded-b-3xl">
                <p class="text-center font-bold text-[16px]">Profile</p>
                <div class="text-center">
                    <div class="text-center inline-block">
                        <!-- <img src="" alt="profile" class="block mx-auto"> -->
                        <div
                            class="mx-auto w-20 h-20 bg-slate-500 rounded-full mt-6"
                        />
                        <div class="relative">
                            <button
                                class="block absolute -translate-y-5 w-full"
                            >
                                <svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    fill="none"
                                    viewBox="0 0 24 24"
                                    stroke-width="1.5"
                                    stroke="currentColor"
                                    class="w-6 h-6 block ml-auto"
                                >
                                    <path
                                        stroke-linecap="round"
                                        stroke-linejoin="round"
                                        d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L10.582 16.07a4.5 4.5 0 01-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 011.13-1.897l8.932-8.931zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0115.75 21H5.25A2.25 2.25 0 013 18.75V8.25A2.25 2.25 0 015.25 6H10"
                                    />
                                </svg>
                            </button>
                        </div>
                    </div>
                </div>
                <div class="text-center">
                    <p class="mt-3 p-1 bg-[#3DB2FF] inline-block rounded">
                        Salis Mazaya
                    </p>
                </div>
            </div>

            <div class="absolute top-0 translate-y-1.5 translate-x-2">
                <button>
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke-width="1.5"
                        stroke="currentColor"
                        class="w-6 h-6 text-white"
                    >
                        <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            d="M9 15L3 9m0 0l6-6M3 9h12a6 6 0 010 12h-3"
                        />
                    </svg>
                </button>
            </div>
        </div>
    </div>
    <Navbar />
</div>
