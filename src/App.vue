<template>
  <link
    href="https://fonts.googleapis.com/css2?family=Josefin+Sans&display=swap"
    rel="stylesheet"
  />
  <link
    rel="stylesheet"
    href="https://unpkg.com/boxicons@latest/css/boxicons.min.css"
  />
  <div>
    <div class="loading-screen" v-show="isLoading">
      <section>
        <div class="content">
          <h2><i class="bx bx-current-location"></i>Bathyscaphe</h2>
          <h2><i class="bx bx-current-location"></i>Bathyscaphe</h2>
        </div>
      </section>
    </div>

    <div class="app-container" v-show="!isLoading">
      <Player></Player>
    </div>
  </div>
</template>

<script>
import Player from "./components/PlayerAndSidebar.vue";

export default {
  components: {
    Player,
  },
  data() {
    return {
      isLoading: true,
    };
  },
  mounted() {
    // Статичное кол во времени симулирующее асинхронный процесс (можно переделать)
    setTimeout(() => {
      this.isLoading = false;
    }, 5000);
  },
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

@import url("https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@400;600&display=swap");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Josefin Sans", sans-serif;
}

body {
  display: flex;
  background: #1d1b31;
  min-height: 100vh;
  align-items: center;
  justify-content: center;
}

.content {
  position: relative;
}

.content h2 {
  display: flex;
  color: #e2e2e2;
  font-size: 3.5vw;
  position: absolute;
  transform: translate(-50%, -50%);
}

.content h2:nth-child(1) {
  color: solid;
  -webkit-text-stroke: 0.15vw #e2e2e2;
}

.content h2:nth-child(2) {
  color: #1d1b31;
  animation: animate 3s ease-in-out infinite;
}

@keyframes animate {
  0%,
  100% {
    clip-path: polygon(
      0% 45%,
      16% 44%,
      33% 50%,
      54% 60%,
      70% 61%,
      84% 59%,
      100% 52%,
      100% 100%,
      0% 100%
    );
  }

  50% {
    clip-path: polygon(
      0% 60%,
      15% 65%,
      34% 66%,
      51% 62%,
      67% 50%,
      84% 45%,
      100% 46%,
      100% 100%,
      0% 100%
    );
  }
}
</style>
