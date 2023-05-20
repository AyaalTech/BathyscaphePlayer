<template>
  <div :id="elementId" />
</template>

<script>
import RTSPtoWEBPlayer from "rtsptowebplayer";

export default {
  name: "PlayerVue",
  data() {
    return {
      elementId: 'player',
      player: null
    };
  },
  mounted() {
    const server = "127.0.0.1:8083";
    const uuid = "Bathyscaphe";
    const source = `http://${server}/stream/receiver/${uuid}`;

    const options = {
      controls: false,
      parentElement: document.getElementById(this.elementId),
      autoplay: true
    };
    this.player = new RTSPtoWEBPlayer(options);
    this.player.load(source);
  },
  beforeUnmount() {
    this.player.destroy();
  }
};
</script>