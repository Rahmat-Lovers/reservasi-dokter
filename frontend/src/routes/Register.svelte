<script>
    import axios from "axios";
    import { navigate } from "svelte-routing";

    let username, name, gender, password, password_confirm;

    let errors_msg = {};

    const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;
</script>

<div class="bg-white">
    <div class="min-h-screen flex items-center mb-5">
        <div class="w-full px-10 lg:px-0">
            <p class="text-[20px] text-center mb-10">Create to your account</p>
            <div>
                <label for="username" class="text-[15px] text-[#5A5A5A]"
                    >Username</label
                >
                {#if errors_msg.username}
                    <p class="text-red-500 text-sm">* {errors_msg.username}</p>
                {/if}
                <input
                    type="text"
                    id="username"
                    class="block outline-none bg-[#E3E2E2] w-full p-3 rounded"
                    bind:value={username}
                />
            </div>
            <div class="mt-5">
                <label for="name" class="text-[15px] text-[#5A5A5A]"
                    >Full Name</label
                >
                {#if errors_msg.name}
                    <p class="text-red-500 text-sm">* {errors_msg.name}</p>
                {/if}
                <input
                    type="text"
                    id="name"
                    class="block outline-none bg-[#E3E2E2] w-full p-3 rounded"
                    bind:value={name}
                />
            </div>
            <div class="mt-5">
                <p class="text-[15px] text-[#5A5A5A]">Select Gender</p>
                {#if errors_msg.gender}
                    <p class="text-red-500 text-sm">* {errors_msg.gender}</p>
                {/if}
                <input
                    type="radio"
                    name="gender"
                    on:change={() => {
                        gender = 1;
                    }}
                />
                <span>Male</span><br />
                <input
                    type="radio"
                    name="gender"
                    on:change={() => {
                        gender = 2;
                    }}
                />
                <span>Female</span><br />
            </div>
            <div class="mt-5">
                <label for="password" class="text-[15px] text-[#5A5A5A]"
                    >Password</label
                >
                {#if errors_msg.password}
                    <p class="text-red-500 text-sm">* {errors_msg.password}</p>
                {/if}
                <input
                    type="password"
                    id="password"
                    class="block outline-none bg-[#E3E2E2] w-full p-3 rounded"
                    bind:value={password}
                />
            </div>
            <div class="mt-5">
                <label for="password-confirm" class="text-[15px] text-[#5A5A5A]"
                    >Password Confirm</label
                >
                {#if errors_msg.password_confirm}
                    <p class="text-red-500 text-sm">* {errors_msg.password_confirm}</p>
                {/if}
                <input
                    type="password"
                    id="password-confirm"
                    class="block outline-none bg-[#E3E2E2] w-full p-3 rounded"
                    bind:value={password_confirm}
                />
            </div>
            <button
                class="block py-3 text-white rounded bg-[#3DB2FF] mt-5 w-full text-[18px]"
                on:click={async () => {
                    errors_msg = {}
                    const keren = {
                        username,
                        name,
                        gender,
                        password,
                        password_confirm,
                    }
                    let thereNull = false;
                    for (const [key, value] of Object.entries(keren)) {
                        if (!value) {
                            errors_msg[key] = 'Tidak boleh kosong'
                            thereNull = true;
                        }
                    }
                    
                    if (password != password_confirm) {
                        errors_msg.password_confirm = 'Password tidak sama!'
                        return
                    }

                    if (thereNull) {
                        return
                    }

                    try {
                        const response = await axios.post(
                            API_BASE_URL + "/register",
                            {
                                username,
                                name,
                                gender,
                                password,
                            }
                        );
                        if (response.data.success) {
                            navigate('/login')
                        }
                    } catch (err) {
                        const details = Object.entries(err.response.data.detail);
                        for (const [key, value] of details) {
                            // console.log(value)
                            errors_msg[key] = value[0].message
                        }
                    }
                }}>Register</button
            >
        </div>
    </div>
</div>
