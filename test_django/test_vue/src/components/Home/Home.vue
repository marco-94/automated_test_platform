<template>
  <div id="home">
    <mt-swipe :auto="4000" style='height: 250px;' class="swipe">
    <mt-swipe-item v-for="(item, index) in imgs" :key="index">
      <img :src="item.img" alt=""/>
    </mt-swipe-item>
</mt-swipe>
    我是首页
  </div>
</template>

<script>
export default {
  name: 'Home',
  data () {
    return {
      imgs: [
        {
          'id': '1002', 'img': 'http://pic5.bbzhi.com/qitabizhi/shishangjiajugaoqingbizhi/shishangjiajugaoqingbizhi_482191_11.jpg'
        },
        {
          'id': '1003', 'img': 'http://pic5.bbzhi.com/qitabizhi/shishangjiajugaoqingbizhi/shishangjiajugaoqingbizhi_481871_11.jpg'
        }
      ]
    }
  },
  created () {
    this.$http.get('getlunbo')
      .then(res => {
        console.log(res.data.message)
        this.imgs = res.data.message
      })
      .catch(err => {
        console.log('异常', err)
      })
  }
}
</script>

<style lang="css" scoped>
.swipe img {
  width: 100%;
  height: 250px;
}
</style>
