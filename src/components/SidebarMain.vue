<template>
  <link href="https://fonts.googleapis.com/css2?family=Josefin+Sans&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://unpkg.com/boxicons@latest/css/boxicons.min.css">
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
              <button class="sidebar-button" :name="name" :value="url">
                <sidebar-item :name="name" :suiid="name" @stream-selected="handleStreamSelected"></sidebar-item>
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
import ToggleButton from './ToggleButton.vue';
import SidebarItem from './SidebarItem.vue';
import configData from './../../RTSPtoWebRTC/config.json';

export default {
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
      config: {},
      streams: {},
      showSidebar: true,
      devices: [],
      selectedDevice: '',
      filteredStreamsData: {},
    };
  },
  methods: {
    toggleSidebar() {
      this.showSidebar = !this.showSidebar;
    },
    updateFilteredStreams() {
      this.filteredStreamsData = this.filteredStreams;
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
};
</script>

<style>
#mySelect {
  font-family: 'Josefin Sans', sans-serif;
}

.sidebar-container {
  position: static;
}

.sidebar-button {
  min-width: 13vw;
  min-height: 6vh;
  font-size: 1vw;
  display: block;
  padding: 1.5vh;
  text-align: center;
  background-color: #1d1b31;
  color: #e2e2e2;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  margin-bottom: 1vh;
  margin-top: 1vh;
  margin-left: 0.5vw;
  transition: background-color 0.4s, color 0.4s, box-shadow 0.4s;
  font-family: 'Josefin Sans', sans-serif;
  box-shadow: 0 0 9px #07070d;
}

.sidebar-button:hover {
  background-color: #e2e2e2;
  color: #21262d;
  box-shadow: 0 0 7px #e2e2e2;
}

.sidebar-button:focus {
  outline: none;
}

.sidebar-background {
  position: absolute;
  min-width: 14vw;
  height: 100%;
  top: 0;
  left: 0;
  background-color: #11101d;
  opacity: 0.95;
  font-family: 'Josefin Sans', sans-serif;
  transition: transform 0.4s cubic-bezier(0.77, 0, 0.175, 1);
  z-index: 1;
}

.sidebar.open .sidebar-background {
  transform: translateX(0);
}

.sidebar.closed .sidebar-background {
  transform: translateX(-100%);
}

.sidebar-header {
  color: #e2e2e2;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  text-align: end;
  margin-top: 4vh;
  font-size: 1.5vw;
  text-shadow: 0 0 5px #23222d;
  margin-bottom: 5vh;
}

.sidebar.open .sidebar-button {
  transition-delay: 0.1s;
}

.logo {
  width: 80%;
  max-width: 150px;
}

.select-container {
  font-size: 1vw;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.custom-select {
  min-width: 13vw;
  min-height: 6vh;
  font-size: 1vw;
  padding: 0.5rem;
  border: none;
  border-radius: 8px;
  background-color: #1E1F29;
  color: #e2e2e2;
  cursor: pointer;
  transition: background-color 0.4s, color 0.4s, box-shadow 0.4s;
  font-family: 'Josefin Sans', sans-serif;
  box-shadow: 0 0 9px #07070d;
  padding-left: 1vw;
}

.custom-select:hover {
  background-color: #e2e2e2;
  color: #21262d;
  box-shadow: 0 0 7px #e2e2e2;
}

.custom-select:focus {
  outline: none;
}

hr.rounded {
  border-top: 0.05vh solid #e2e2e2;
  border-radius: 15px;
  width: 4vw;
  margin-top: 3vh;
  margin-bottom: 3vh;
}
</style>