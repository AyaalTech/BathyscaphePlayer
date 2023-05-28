<template>
  <sidebar></sidebar>
  <div class="fullscreen-player">
    <player-vue></player-vue>
  </div>
</template>

<script>
import PlayerVue from './components/PlayerVue.vue';
import Sidebar from './components/SidebarMain.vue';

export default {
  components: {
    PlayerVue,
    Sidebar
  },
};
</script>

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
</style>