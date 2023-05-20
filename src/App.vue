<template>
  <Sidebar />
  <div class="fullscreen-player">
    <PlayerVue />
  </div>
</template>

<style>
.fullscreen-player {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
}

@import url("assets/reset.css");
@import url("assets/sidebar.css");
</style>

<script>
import PlayerVue from "./components/PlayerVue.vue";
import Sidebar from "./components/Sidebar.vue";
export default {
  name: 'App',
  components: {
    PlayerVue,
    Sidebar
  },
}
</script>