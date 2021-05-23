<template>
  <div class="container text-center">
    <div class="form col-12">
      <input 
        :value="data"
        @input="insertData"
        class="col-11" 
        type="text" 
        placeholder="Search">
      <span class="col-1"><i class="fas fa-search fs-4"></i></span>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'SearchBar',
  data: function () {
    return {
      data: '',
    }
  },
  methods: {
    insertData: function (event) {
      this.data = event.target.value
      this.$store.dispatch('movie/searchData', this.data)
    }
  },
  computed: {
    ...mapState('movie', ['searchResult'])
  }
}
</script>

<style scoped>
  .container{
    max-width: 720px;
    margin: auto;
    padding: 0 50px;
  }

  input{
    padding:0;
    border-radius: 0;
    border: none;
    font-size: 20px;
    color: #bbb;
    background:none;
    letter-spacing: 1px;
    word-spacing: 10px;
    padding: 0;
    line-height: 25px;
    outline: none;
  }

  .form{
    padding: 10px 2px;
    border: 0.25rem solid #F47B0F;
    background-color: #1E1F26;
  }

</style>