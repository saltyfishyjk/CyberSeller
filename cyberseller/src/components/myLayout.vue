<template>
    <div>
        <div class="header">Title</div>
        <div class="navbar">Category</div>
        <div class="main">Page</div>
    </div>
</template>

<style scoped>
/* 头部样式 */
.header {
    position: absolute;
    line-height: 50px;
    top: 0px;
    left: 0px;
    right: 0px;
    background-color: rgb(225, 225, 225);
}

/* 左侧样式 */
.navbar {
    position: absolute;
    width: 230px;
    top: 50px;
    /* 距离上面50像素 */
    left: 0px;
    bottom: 0px;
    overflow-y: auto;
    /* 当内容过多时y轴出现滚动条 */
    background-color: rgb(225, 225, 225);
}

/* 主区域 */
.main {
    position: center;
    top: 50px;
    left: 230px;
    bottom: 0px;
    right: 0px;
    /* 距离右边0像素 */
    padding: 10px;
    overflow-y: auto;
    /* 当内容过多时y轴出现滚动条 */
    /* background-color: red; */
}
</style>