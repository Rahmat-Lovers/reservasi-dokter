<script>
    import "./index.css";
    import { Router, Route, navigate } from "svelte-routing";
    import Index from "./routes/Index.svelte";
    import Login from "./routes/Login.svelte";
    import Dashboad from "./routes/Dashboad.svelte";
    import Register from "./routes/Register.svelte";
    import axios from "axios";
    import cookie from "cookie";

    let token;

    (async () => {
        token = cookie.parse(document.cookie).login;
        const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;
        if (window.location.href.includes("/dashboard")) {
            try {
                await axios.get(API_BASE_URL + "/loged", {
                    headers: {
                        Authorization: "Bearer " + token,
                    },
                });
            } catch {
                navigate("/login");
            }
        }
    })();

    export let url = "";
</script>

<main>
    <div class="max-w-lg mx-auto">
        <Router {url}>
            <Route path="/" component={Index} />
            <Route path="/login" component={Login} />
            <Route path="/register" component={Register} />
            <Route path="/dashboard" component={Dashboad} />
        </Router>
    </div>
</main>
