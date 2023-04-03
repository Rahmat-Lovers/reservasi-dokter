<script>
    import axios from "axios";
    import cookie, { parse } from "cookie";
    import { getDistanceYear } from "./../helpers";

    const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

    let loading = true;
    let token;
    let data;
    let doctors;

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

{#if loading}
    <p>Loading</p>
{:else}
    <div class="container mx-auto">
        <p>{data.name}</p>

        <div class="mt-2 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
            {#each doctors as doctor}
                <div
                    class="text-sm flex items-center cursor-pointer hover:bg-blue-400"
                >
                    <div class="w-28 h-28 bg-slate-500 rounded-full" />
                    <div class="ml-2">
                        <p>Dr. {doctor.customer.name}</p>
                        <p>
                            {#each doctor.specialist as specialist}
                                <span class="mr-1">{specialist.name},</span>
                            {/each}
                        </p>
                        <p>{getDistanceYear(new Date(doctor.experience_since))} Tahun</p>
                    </div>
                </div>
            {/each}
        </div>
    </div>
{/if}
