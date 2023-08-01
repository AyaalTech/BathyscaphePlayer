<template>
  <li>
    <a>{{ name }}</a>
  </li>
</template>

<script>
export default {
  props: {
    name: String,
    url: String,
  },
};
</script>
