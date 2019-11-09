<template>
  <div id="app">
    <mt-header title="信息管理系统">
      <mt-button router-link="'/'" icon="back" slot="left">返回</mt-button>
      <mt-button icon="more" slot="right"></mt-button>
    </mt-header>

    <!--路由组件出口-->
    <router-view/>

    <!--底部栏-->
    <mt-tabbar v-model="selected">
  <mt-tab-item id="home">
    <img slot="icon" src="./assets/test.jpg">
    首页
  </mt-tab-item>
  <mt-tab-item id="会员">
    <img slot="icon" src="./assets/test.jpg">
    会员
  </mt-tab-item>
  <mt-tab-item id="购物车">
    <img slot="icon" src="./assets/test.jpg">
    购物车
  </mt-tab-item>
  <mt-tab-item id="搜索">
    <img slot="icon" src="./assets/test.jpg">
    搜索
  </mt-tab-item>
</mt-tabbar>

  </div>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      selected: ''
    }
  },
  watch: {
    selected: function (newV, oldV) {
      console.log(newV, oldV)
      console.log(this.selected)
      this.$router.push({name: this.selected})
    }
  }
}
</script>

<style>
*{
  padding: 0;
  margin: 0;
}
</style>
