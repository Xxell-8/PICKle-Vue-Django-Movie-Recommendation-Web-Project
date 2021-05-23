<template>
  <div class="col-auto my-2" >
    <div class="card h-100">
      <img
        :src="cardUrl" 
        :alt="cardName"
      >
    </div>
  </div>
</template>

<script>
export default {
  name: 'RecommendCard',
  props: {
    cardName: {
      type: String,
    }
  },
  computed: {
    cardUrl: function () {
      return `../../assets/${this.cardName}.svg`
    }
  }

}
</script>

<style>

</style>