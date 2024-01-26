<script>
  // import { onMount } from "svelte";

  import Player from "./lib/Player.svelte";
  import Channel from "./lib/Channel.svelte";
  // let Player, Channel;
  // async function loadPlayer() {
  //   Player = (await import("./lib/Player.svelte")).default;
  // }
  // async function loadChannel() {
  //   Channel = (await import("./lib/Channel.svelte")).default;
  // }
  // onMount(()=> {
  //   loadPlayer();
  //   loadChannel();
  // })
</script>

<main>
  <Channel></Channel>
  <Player></Player>
  <!-- {#if Channel}
  <svelte:component this={Channel} />
  {/if}
  {#if Player}
    <svelte:component this={Player} />
  {/if} -->
</main>

<style>
  main {
    width: 100vw;
    height: 100vh;
    display: grid;
    grid-template-columns: 1fr 8fr;
    grid-template-rows: 1fr;
    gap: 0 0;
    grid-template-areas: ". .";
  }
</style>
