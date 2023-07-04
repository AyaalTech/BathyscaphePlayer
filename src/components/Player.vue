<template>
  <link href="https://fonts.googleapis.com/css2?family=Josefin+Sans&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://unpkg.com/boxicons@latest/css/boxicons.min.css">
  <div class="fullscreen-player">
    <div :id="elementId" />
  </div>
  <div class="sidebar-container">
    <div class="sidebar-wrapper">
      <aside :class="['sidebar', { 'open': showSidebar, 'closed': !showSidebar }]">
        <div class="sidebar-background">
          <div class="sidebar-header">
            <p style="font-weight: bolder;"><i class="bx bx-current-location"></i> Bathyscaphe</p>
          </div>
          <hr class="rounded">
          <div class="select-container">
              <div><p style="font-size: 1.2vw; color: #e2e2e2; margin-bottom: 1vh;">Currently streaming:</p> {{ selected }}</div>
                <select class="custom-select" v-model="selectedDevice" @change="updateFilteredStreams">
                  <option id="mySelect" disabled value="">Select the drone</option>
                  <option v-for="device in devices" :key="device">{{ device }}</option>
                </select>
          </div>
          <hr class="rounded">
          <ul>
            <li v-for="(url, name) in filteredStreams" :key="name">
              <button class="sidebar-button" :name="name" :value="url" @click="handleStreamSelected(name)" :disabled="streamErrors.includes(name)">
                <sidebar-item :name="name" :uuid="name"></sidebar-item>
              </button>
            </li>
          </ul>
        </div>
      </aside>
      <toggle-button :show-sidebar="showSidebar" @toggle-sidebar="toggleSidebar"></toggle-button>
    </div>
  </div>
</template>

<script>
import RTSPtoWEBPlayer from "rtsptowebplayer";
import ToggleButton from './ToggleButton.vue';
import SidebarItem from './SidebarItem.vue';
import configData from './../../RTSPtoWebRTC/config.json';

export default {
  name: "PlayerVue",
  computed: {
    filteredStreams() {
      return Object.entries(this.streams).reduce((filtered, [name, stream]) => {
        if (stream.deviceNumber.toString() === this.selectedDevice) {
          filtered[name] = stream.url;
        }
        return filtered;
      }, {});
    },
  },
  data() {
    return {
      streams: {},
      showSidebar: true,
      devices: [],
      selectedDevice: '',
      elementId: 'player',
      streamErrors: [],
      player: null,
    };
  },
  methods: {
    toggleSidebar() {
      this.showSidebar = !this.showSidebar;
    },
    updateFilteredStreams() {
      this.filteredStreamsData = this.filteredStreams;
    },
    handleStreamSelected(uuid) {
      this.uuid = uuid;
      const server = "127.0.0.1:8083";
      const source = `http://${server}/stream/receiver/${uuid}`;

      this.player.destroy();

      const options = {
        controls: false,
        parentElement: document.getElementById(this.elementId),
        autoplay: true
      };
      this.player = new RTSPtoWEBPlayer(options);
      this.player.load(source);
    },
  },
  created() {
    this.config = configData;
    this.streams = configData.streams;
    this.devices = [...new Set(Object.values(this.streams).map((stream) => stream.deviceNumber))];
    this.selectedDevice = this.devices[0].toString();
  },
  components: {
    SidebarItem,
    ToggleButton
  },
  mounted() {
    const server = "127.0.0.1:8083";
    const uuid = "Japan";
    const source = `http://${server}/stream/receiver/${uuid}`;

    const options = {
      controls: false,
      parentElement: document.getElementById(this.elementId),
      autoplay: true
    };
    this.player = new RTSPtoWEBPlayer(options);
    this.player.load(source);
  },
  beforeUnmounted() {
    this.player.destroy();
  }
};
</script>

<style>
  @import url("../assets/sidebar.css");

  .fullscreen-player {
  position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    overflow: hidden;
    /* fix scaling */
  }
</style>