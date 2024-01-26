<script>
    import Hls from "hls.js";
    import DPlayer from "dplayer";
    import { onMount } from "svelte";
    import { DPstore } from "../store";
    let dp;
    onMount(() => {
        dp = new DPlayer({
            container: document.getElementById("dplayer"),
            video: {
                url: "http://tv.pull.hebtv.com/jishi/weishipindao.m3u8?t=2510710360&k=3944fff7fdd8f8caf6adce2c9a0ef126",
                live: true,
                type: "customHls",
                customType: {
                    customHls: function (video, player) {
                        const hls = new Hls();
                        hls.loadSource(video.src);
                        hls.attachMedia(video);
                    },
                },
            },
        });
        DPstore.set(dp);
    });
</script>

<div id="dplayer"></div>
