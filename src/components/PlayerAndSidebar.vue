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
        // You can now use the brokenStreams list to update the disabled state of buttons in your template.
        // You might want to add the brokenStreams to your component's data and use it in the template to disable buttons.
        // For example, you can create a data property called `brokenStreams` and set it using `this.brokenStreams = brokenStreams;`
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
</style>