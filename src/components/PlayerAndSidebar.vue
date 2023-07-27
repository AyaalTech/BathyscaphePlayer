<template>
  <link href="https://fonts.googleapis.com/css2?family=Josefin+Sans&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://unpkg.com/boxicons@latest/css/boxicons.min.css">
  <div class="fullscreen-player">
    <div :id="elementId" />
  </div>
  <div class="loader-container" v-if="isLoading">
    <div class="loader"></div>
    <p class="loading-text"><i class='bx bx-hourglass hourglass-tilt'></i></p>
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
            <li v-for="(stream, name) in filteredStreams" :key="name">
              <button class="sidebar-button" :name="name" :value="stream.url" @click="handleStreamSelected(name)" :disabled="!stream.status">
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
import axios from 'axios';
import RTSPtoWEBPlayer from "rtsptowebplayer";
import ToggleButton from './ToggleButton.vue';
import SidebarItem from './SidebarItem.vue';
import configData from './../../RTSPtoWeb/config.json';

export default {
  name: "PlayerVue",
  computed: {
    filteredStreams() {
      return Object.entries(this.streams).reduce((filtered, [name, stream]) => {
        if (stream.deviceNumber.toString() === this.selectedDevice) {
          const streamStatus = this.checkStreamStatus(stream.url);
          filtered[name] = { url: stream.url, status: streamStatus };
        }
        return filtered;
      }, {});
    },
  },
  data() {
    return {
      isLoading: false,
      config: {},
      streams: {},
      showSidebar: true,
      devices: [],
      selectedDevice: '',
      elementId: 'player',
    };
  },
  methods: {
    async fetchStreams() {
      const serverUrl = 'http://127.0.0.1:8083/streams';
      try {
        const response = await axios.get(serverUrl, {
          auth: {
            username: 'demo',
            password: 'demo'
          }
        });
        const streamsData = response.data.payload;
        const brokenStreams = [];

        Object.entries(streamsData).forEach(([uuid, streamInfo]) => {
          Object.entries(streamInfo.channels).forEach(([channel, channelInfo]) => {
            if (!channelInfo.status || channelInfo.status !== 1) {
              brokenStreams.push({
                uuid,
                channel,
                url: channelInfo.url
              });
            }
          });
        });

        console.log('Broken Streams:', brokenStreams);
      } catch (error) {
        console.error('Error fetching streams:', error);
      }
    },
    async checkStreamStatus(url) {
      try {
        const response = await fetch(url);
        return response.ok;
      } catch (error) {
        return false;
      }
    },
    toggleSidebar() {
      this.showSidebar = !this.showSidebar;
    },
    handleStreamSelected(uuid) {
      this.isLoading = true;
      this.uuid = uuid;
      const server = "127.0.0.1:8083";
      const channel = "0";
      const source = `http://${server}/stream/${uuid}/channel/${channel}/webrtc?uuid=${uuid}/&channel=${channel}`;

      this.player.destroy();

      const options = {
        controls: false,
        parentElement: document.getElementById(this.elementId),
        autoplay: true
      };
      this.player = new RTSPtoWEBPlayer(options);
      this.player.load(source);
      setTimeout(() => {
        this.isLoading = false;
      }, 1500); 
    },
  },
  created() {
    this.config = configData;

    this.streams = Object.entries(this.config.streams).reduce((acc, [uuid, streamData]) => {
      if (streamData.channels && typeof streamData.channels === 'object') {
        Object.values(streamData.channels).forEach(channel => {
          acc[uuid] = {
            deviceNumber: channel.deviceNumber,
            url: channel.url
          };
        });
      }
      return acc;
    }, {});

    this.devices = [...new Set(Object.values(this.streams).map((stream) => stream.deviceNumber))];
    this.selectedDevice = this.devices[0].toString();
    this.fetchStreams();
  },
  components: {
    SidebarItem,
    ToggleButton
  },
  mounted() {
    const server = "127.0.0.1:8083";
    const uuid = "demo";
    const channel = "0";
    const source = `http://${server}/stream/${uuid}/channel/${channel}/webrtc?uuid=${uuid}/&channel=${channel}`;

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

<style>
  @import url("../assets/sidebar.css");

  .fullscreen-player {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    overflow: hidden;
  }

  .loader-container {
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 100;
    position: absolute;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.6);
  }

  .loader {
    border: 0.4vw solid #23222d; 
    border-top: 0.4vw solid #e3e3e3; 
    border-bottom: 0.4vw solid #e3e3e3; 
    border-radius: 50%;
    width: 7vw;
    height: 7vw;
    animation: spin 4s linear infinite;
  }

  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }

  .loading-text {
    position: absolute;
    font-size: 2.5vw;
    color: #fff;  
    text-align: center; 
  }

  .hourglass-tilt {
    animation: tilt 2.5s ease-in-out infinite;
  }

  @keyframes tilt {
    0%, 100% {
      transform: rotate(0deg);
    }
    50% {
      transform: rotate(180deg);
    }
  }
</style>