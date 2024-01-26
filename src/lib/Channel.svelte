<script>
    import { onMount } from "svelte";
    import { DPstore, Channel } from "../store";
    import Hls from "hls.js";
    let dp;
    const unsubscribe = DPstore.subscribe((value) => {
        dp = value;
    });
    // let promise =  get_list();
    // async function get_list() {
    //     const res = fetch("https://tv.cdmn.eu.org/");
    //     const list = (await res).json();
    //     return list;
    // }
    // onMount(() => {
    //     promise = get_list();
    // });
    function change(url) {
        dp.switchVideo({
            url: url,
            type: "customHls",
            customType: {
                customHls: function (video, player) {
                    const hls = new Hls();
                    hls.loadSource(video.src);
                    hls.attachMedia(video);
                },
            },
        });
        dp.play();
    }
</script>

<div id="channel">
    <h1>iptv😎</h1>
    <!-- {#await promise}
        <h3>loading</h3>
    {:then list} 
        {#each list as { name, url }}
        <button on:click={() => change(url)}>{name}</button>
        {/each}
    {/await} -->
    <!-- <hr /> -->
    {#each Channel as { name, url }}
        <button on:click={() => change(url)}>{name}</button>
    {/each}
</div>

<style>
    #channel {
        width: 10rem;
        background-color: gray;
        display: flex;
        flex-direction: column;
        overflow: scroll;
        overflow-x: hidden;
    }
    #channel::-webkit-scrollbar {
        width: 10px;
    }
    #channel::-webkit-scrollbar-thumb {
        background: #ccc;
        border-radius: 5px;
    }
    button {
        border: none;
        padding: 0;
        background: none;
        padding: 0.6rem;
        font-size: 1.1rem;
    }
    #channel button:hover {
        background-color: aqua;
        color: aliceblue;
    }
</style>
