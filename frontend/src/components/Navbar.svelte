<script>
    import { Link } from "svelte-routing";
</script>

<div
    class=" w-[360px] h-12 fixed bottom-0 left-[50%] -translate-x-1/2 flex justify-around items-center flex-wrap mx-auto font-semibold bg-slate-50 border-t border-gray-200"
>
    <Link to="/dashboard">
        <div class="relative w-10 h-auto">
            <div class=" w-6 h-6 top-0 left-0 translate-x-2 rounded-full">
                <svg
                    aria-hidden="true"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="1.5"
                    viewBox="0 0 24 24"
                    xmlns="http://www.w3.org/2000/svg"
                >
                    <path
                        d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                    />
                </svg>
            </div>
            <span class=" block w-7 h-auto mx-auto text-[8px] tracking-wide"
                >Beranda</span
            >
        </div>
    </Link>

    <Link to="/dashboard/search">
        <div class="relative w-auto h-auto text-center">
            <div class=" w-6 h-6 top-0 left-0 translate-x-2 rounded-full">
                <svg
                    aria-hidden="true"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="1.5"
                    viewBox="0 0 24 24"
                    xmlns="http://www.w3.org/2000/svg"
                >
                    <path
                        d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                    />
                </svg>
            </div>
            <span class=" block w-auto h-auto mx-auto text-[8px] tracking-wide"
                >Cari Dokter</span
            >
        </div>
    </Link>

    <div class="relative w-10 h-auto text-center">
        <div class=" w-6 h-6 top-0 left-0 translate-x-2 rounded-full">
            <img src="/img/history.png" alt="icon history" />
        </div>
        <span class=" block w-7 h-auto mx-auto text-[8px] tracking-wide"
            >Riwayat</span
        >
    </div>

    <div class="relative w-10 h-auto text-center">
        <div class=" w-6 h-6 top-0 left-0 translate-x-2 rounded-full">
            <svg
                aria-hidden="true"
                fill="none"
                stroke="currentColor"
                stroke-width="1.5"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
            >
                <path
                    d="M17.982 18.725A7.488 7.488 0 0012 15.75a7.488 7.488 0 00-5.982 2.975m11.963 0a9 9 0 10-11.963 0m11.963 0A8.966 8.966 0 0112 21a8.966 8.966 0 01-5.982-2.275M15 9.75a3 3 0 11-6 0 3 3 0 016 0z"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                />
            </svg>
        </div>
        <span class=" block w-7 h-auto mx-auto text-[8px] tracking-wide"
            >Akun</span
        >
    </div>
</div>
