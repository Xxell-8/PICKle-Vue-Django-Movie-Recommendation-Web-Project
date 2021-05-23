<template>
  <div class="container mt-5">
    <div class="row gap-3 justify-content-center">
      <SearchListItem
        v-for="(movie, idx) in searchResult"
        :key="idx"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import SearchListItem from '@/components/movies/SearchListItem'

export default {
  name: 'SearchList',
  components: {
    SearchListItem,
  },
  computed: {
    ...mapState('movie', ['searchResult'])
  }
}
</script>

<style>

</style>