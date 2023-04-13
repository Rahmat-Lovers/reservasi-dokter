<script>
    import { onDestroy, onMount } from "svelte";

    import Loading from "../components/Loading.svelte";
    import Navbar from "../components/Navbar.svelte";
    import axios from "axios";
    import cookie from "cookie";
    import { getDistanceYear } from "../helpers";

    const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

    let loading;
    let token;
    let data;
    let doctors = [];

    onDestroy(async () => {
        loading = true;
    });

    onMount(async () => {
        loading = true;
        token = cookie.parse(document.cookie).login;
        // const response = await axios.get(API_BASE_URL + "/me", {
        //     headers: {
        //         Authorization: "Bearer " + token,
        //     },
        // });
        // data = response.data.data;

        const responseDoctor = await axios.get(API_BASE_URL + "/doctors", {
            headers: {
                Authorization: "Bearer " + token,
            },
        });
        doctors = responseDoctor.data.data;

        loading = false;
    });
</script>

<Loading bind:isLoading={loading} />

<div class="mx-3">
    <div class="main overflow-y-auto">
        <div class="bg-[#3DB2FF] my-3 w-full rounded p-5 mt-5">
            <div class="flex items-center">
                <div class="h-14 w-14 bg-white rounded-full" />
                <div class="ml-4 text-white">
                    <p>Dr. Sekeren</p>
                    <p class="text-sm">Ahli Keren</p>
                </div>
            </div>
        </div>

        <div class="mt-4">
            <p>Pilih Dokter</p>

            <div class="flex gap-2 overflow-x-auto">
                <div class="flex-none bg-[#D9D9D9] h-12 w-12 rounded-full" />
                <div class="flex-none bg-[#D9D9D9] h-12 w-12 rounded-full" />
                <div class="flex-none bg-[#D9D9D9] h-12 w-12 rounded-full" />
                <div class="flex-none bg-[#D9D9D9] h-12 w-12 rounded-full" />
                <div class="flex-none bg-[#D9D9D9] h-12 w-12 rounded-full" />
                <div class="flex-none bg-[#D9D9D9] h-12 w-12 rounded-full" />
                <div class="flex-none bg-[#D9D9D9] h-12 w-12 rounded-full" />
                <div class="flex-none bg-[#D9D9D9] h-12 w-12 rounded-full" />
                <div class="flex-none bg-[#D9D9D9] h-12 w-12 rounded-full" />
                <div class="flex-none bg-[#D9D9D9] h-12 w-12 rounded-full" />
                <div class="flex-none bg-[#D9D9D9] h-12 w-12 rounded-full" />
                <div class="flex-none bg-[#D9D9D9] h-12 w-12 rounded-full" />
                <div class="flex-none bg-[#D9D9D9] h-12 w-12 rounded-full" />
                <div class="flex-none bg-[#D9D9D9] h-12 w-12 rounded-full" />
                <div class="flex-none bg-[#D9D9D9] h-12 w-12 rounded-full" />
                <div class="flex-none bg-[#D9D9D9] h-12 w-12 rounded-full" />
            </div>
        </div>

        <div class="mt-4">
            <p>Rekomendasi Dokter</p>

            <div class="grid gap-2 grid-cols-2 xl:grid-cols-3 overflow-y-auto">
                {#each doctors as doctor}
                    <div
                        class="p-3 border rounded-md text-[#5A5A5A] hover:bg-[#3DB2FF] hover:text-white"
                    >
                        <div class="w-12 h-12 rounded-full bg-yellow-200" />
                        <p class="text-sm font-bold">
                            Dr. {doctor.customer.name}
                        </p>
                        <p class="text-xs">
                            Spesialis {doctor.specialist
                                .map((x) => x.name)
                                .join(", ")}
                        </p>
                    </div>


                {/each}
            </div>
        </div>
    </div>

    <Navbar />
</div>
