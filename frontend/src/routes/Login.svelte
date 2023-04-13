<script>
    import Swal from "sweetalert2";
    import axios from "axios";
    import cookie from "cookie";
    import { navigate } from "svelte-routing";

    let username, password;

    const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;
</script>

<div class="bg-white">
    <div class="min-h-screen flex items-center">
        <div class="w-full px-10 lg:px-0">
            <p class="text-[20px] text-center mb-10">Login to your account</p>
            <div>
                <label for="username" class="text-[15px] text-[#5A5A5A]"
                    >Username</label
                >
                <input
                    type="text"
                    id="username"
                    class="block outline-none bg-[#E3E2E2] w-full p-3"
                    bind:value={username}
                />
            </div>
            <div class="mt-5">
                <label for="password" class="text-[15px] text-[#5A5A5A]"
                    >Password</label
                >
                <input
                    type="password"
                    id="password"
                    class="block outline-none bg-[#E3E2E2] w-full p-3"
                    bind:value={password}
                />
            </div>
            <button
                class="block py-3 text-white rounded bg-[#3DB2FF] mt-5 w-full text-[18px]"
                on:click={async () => {
                    if (!username || !password) {
                        await Swal.fire({
                            icon: "info",
                            text: "Cek kembali username / password",
                        });
                        return;
                    }

                    try {
                        const response = await axios.post(
                            API_BASE_URL + "/login",
                            {
                                username,
                                password,
                            }
                        );
                        const result = response.data;
                        const token = result.data.token;
                        document.cookie = cookie.serialize("login", token);
                        navigate("/dashboard");
                    } catch (err) {
                        console.log(err);
                        Swal.fire({
                            icon: "error",
                            text: "Username atau password salah!",
                        });
                    }
                }}>Login</button
            >
        </div>
    </div>
</div>
