<template>
    <div class="sidebar" :class="isOpened ? 'open' : ''" :style="cssVars">
      <div class="logo-details" style="margin: 6px 14px 0 14px">
        <img v-if="menuLogo" :src="menuLogo" alt="menu-logo" class="menu-logo icon">
        <i v-else class="bx icon" :class="menuIcon"></i>
        <div class="logo_name">{{ menuTitle }}</div>
        <i id="btn" class="bx" :class="isOpened ? 'bx bx-low-vision' : 'bx bx-show-alt'" @click="isOpened = !isOpened"></i>
      </div>
  
      <div class="sidebar-content" style="display: flex; flex-direction: column; justify-content: space-between; flex-grow: 1; max-height: calc(100% - 60px);">
        <div id="my-scroll" style="margin: 6px 14px 0 14px">
          <ul class="nav-list" style="overflow: visible">
            <li id="links_search" v-if="isSearch" @click="isOpened = true">
              <i class="bx bx-search"></i>
              <input type="text" :placeholder="searchPlaceholder" @input="$emit('search-input-emit', $event.target.value)">
            </li>
    
            <li v-for="(menuItem, index) in menuItems" :key="index" :id="'links_' + index">
              <router-link v-if="isUsedVueRouter" :to="menuItem.link">
                <i class="bx" :class="menuItem.icon || 'bx-square-rounded'"></i>
                <span class="links_name">{{ menuItem.name }}</span>
              </router-link>
              <a v-else @click.stop.prevent="$emit('menuItemClcked', menuItem.link)" :href="menuItem.link">
                <i class="bx" :class="menuItem.icon || 'bx-square-rounded'"></i>
                <span class="links_name">{{ menuItem.name }}</span>
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  //import config from '../../RTSPtoWebRTC/config.json'
  export default {
    name: 'SidebarMenu',
    props: {
      // Menu settings
      isMenuOpen: {
        type: Boolean,
        default: true,
      },
      isUsedVueRouter: {
        type: Boolean,
        default: false,
      },
      menuTitle: {
        type: String,
        default: 'Bathyscaphe',
      },
      menuLogo: {
        type: String,
        default: '',
      },
      menuIcon: {
        type: String,
        default: 'bx bx-current-location',
      },
      isPaddingLeft: {
        type: Boolean,
        default: true,
      },
      menuOpenedPaddingLeftBody: {
        type: String,
        default: '250px',
      },
      menuClosedPaddingLeftBody: {
        type: String,
        default: '78px',
      },
      //Menu items
      menuItems: {
          type: Array,
          default: () => [
            {
              link: '#',
              name: 'Bot number 1',
              icon: 'bx-bot',
            },
            {
              link: '#',
              name: 'Bot number 2',
              icon: 'bx-bot',
            },
            {
              link: '#',
              name: 'Bot number 3',
              icon: 'bx-bot',
            },
          ],
        },
        //Search
        isSearch: {
          type: Boolean,
          default: true,
        },
        searchPlaceholder: {
          type: String,
          default: 'Search...',
        },
        //Styles
        logoDetailsColor: {
          type: String,
          default: '#21262d',
        },
        searchInputTextColor: {
          type: String,
          default: '#fff',
        },
        bgColor: {
          type: String,
          default: '#21262d',
        },
        secondaryColor: {
          type: String,
          default: '#161b22',
        },
        homeSectionColor: {
          type: String,
          default: '#0d1117',
        },
        logoTitleColor: {
          type: String,
          default: '#fff',
        },
        iconsColor: {
          type: String,
          default: '#fff',
        },
        menuItemsHoverColor: {
          type: String,
          default: '#fff',
        },
        menuItemsTextColor: {
          type: String,
          default: '#fff',
        },
      },
      data() {
        return {
          closedOpacity: 0,
          isOpened: false,
        }
      },
      mounted() {
        this.isOpened = this.isMenuOpen
      },
      computed: {
        cssVars() {
          return {
            // '--padding-left-body': this.isOpened ? this.menuOpenedPaddingLeftBody : this.menuClosedPaddingLeftBody,
            '--bg-color': this.bgColor,
            '--secondary-color': this.secondaryColor,
            '--home-section-color': this.homeSectionColor,
            '--logo-title-color': this.logoTitleColor,
            '--logo-details-color': this.isOpened ? '#fff' : '#21262d',
            '--icons-color': this.iconsColor,
            '--serach-input-text-color': this.searchInputTextColor,
            '--menu-items-hover-color': this.menuItemsHoverColor,
            '--menu-items-text-color': this.menuItemsTextColor,
            '--closed-opacity': !this.isOpened ? this.closedOpacity : '',
            '--sidebar-background': this.isOpened ? '#21262d' : 'transparent',
            '--text-align': this.isOpened ? 'right' : 'center',
          }
        },
      },
      watch: {
        isOpened() {
          window.document.body.style.paddingLeft =
            this.isOpened && this.isPaddingLeft
              ? this.menuOpenedPaddingLeftBody
              : this.menuClosedPaddingLeftBody
        },
      },
    }
  </script>