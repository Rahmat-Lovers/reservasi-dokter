<script>
    import { Link } from "svelte-routing";
</script>

<div class="min-h-screen flex items-center bg-gradient-to-b from-[#89DDFC] via-[#09A6F3] to-[#1363DF]">
    <div class="w-full px-10">
        <div class="translate-y-10">
            <p class="font-semibold text-[32px] text-white">Selamat Datang</p>
            <p class="font-medium text-[20px] text-white">HaloMat App</p>
            <button class="py-2 bg-[#1363DF] w-full text-white rounded mt-10">
                <p class="font-medium text-[18px]">Register</p>
            </button>
            <Link to="/login">
                <button class="py-2 bg-[#F3F3F3] w-full text-[#5A5A5A] rounded mt-4">
                    <p class="font-medium text-[18px]">Login</p>
                </button>
            </Link>
        </div>
        <div class="bottom-0 m-4 fixed text-white italic z-auto left-0 right-0">
            <p class="text-center">Powered by @RahmatLover</p>
        </div>
    </div>

</div>
