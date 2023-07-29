<template>
  <link href="https://fonts.googleapis.com/css2?family=Josefin+Sans&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://unpkg.com/boxicons@latest/css/boxicons.min.css">
  <div>
    <div class="loading-screen" v-if="isLoading">
      <p style="font-weight: bolder; color: #e2e2e2; animation: pulsate 2s ease-in-out infinite;"><i class="bx bx-current-location"></i> Bathyscaphe</p>
    </div>

    <div class="app-container" v-else>
      <Player></Player>
    </div>
  </div>
</template>

<script>
import Player from './components/PlayerAndSidebar.vue';

export default {
  components: {
    Player
  },
  data() {
    return {
      isLoading: true
    };
  },
  mounted() {
    setTimeout(() => {
      this.isLoading = false;
    }, 4000);
  }
};
</script>

<style>
  @import url("assets/reset.css");
  
  .app-container {
    justify-content: center;
    align-items: center;
    height: 100vh;
    width: 100vw;
    background-color: #000000;
  }

  .loading-screen {
    font-family: 'Josefin Sans', sans-serif;
    justify-content: center;
    align-items: center;
    display: flex;
    position: fixed;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    background-color: #11101d;
    color: #ffffff;
    font-size: 2rem;
  }

  @keyframes pulsate {
    0% {
      transform: scale(1);
    }
    50% {
      transform: scale(1.4);
    }
    100% {
      transform: scale(1);
    }
  }
</style>
