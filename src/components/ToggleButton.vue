<template>
  <button class="toggle-button" @click="toggleSidebar">
    {{ buttonText }}
    <i
      :class="['bx', { 'bx-low-vision': showSidebar, 'bx-show': !showSidebar }]"
    ></i>
  </button>
</template>

<script>
export default {
  props: {
    showSidebar: {
      type: Boolean,
      default: true,
    },
  },
  computed: {
    buttonText() {
      return this.showSidebar ? "Hide menu" : "Show menu";
    },
  },
  methods: {
    toggleSidebar() {
      this.$emit("toggle-sidebar");
    },
  },
};
</script>

<style>
.toggle-button {
  background-color: #1e1f29;
  margin-left: 1vw;
  z-index: 50;
  position: absolute;
  bottom: 1vh;
  margin-left: 0.5vw;
  min-width: 13vw;
  min-height: 6vh;
  color: #e2e2e2;
  border: none;
  border-radius: 8px;
  font-size: 1vw;
  vertical-align: middle;
  font-weight: 900;
  cursor: pointer;
  transition: background-color 0.4s, color 0.4s;
  font-family: "Josefin Sans", sans-serif;
  box-shadow: 0 0 9px #07070d;
}

.toggle-button i {
  vertical-align: middle;
  font-size: 1vw;
  margin-right: 0.5rem;
}

.toggle-button:hover {
  background-color: #e2e2e2;
  color: #21262d;
  box-shadow: 0 0 7px #e2e2e2;
}

.toggle-button:focus {
  outline: none;
}
</style>
