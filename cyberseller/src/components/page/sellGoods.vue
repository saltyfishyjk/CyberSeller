<template>
    <div style="text-align: center;width: 20%;margin-left: 40%;margin-top: 30px;">

    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px">
        <el-form-item label="商品名" prop="name">
            <el-input v-model="ruleForm.name" style="width: 300px"></el-input>
        </el-form-item>
        <el-form-item label="价格" prop="price">
            <el-input v-model="ruleForm.price" style="width: 300px"></el-input>
        </el-form-item>
        <el-form-item label="商品图片">
            <input type="file"  @change="getImageFile" id="img">
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm')">发布商品</el-button>
            <el-button @click="resetForm('ruleForm')">重置</el-button>
        </el-form-item>
    </el-form>
        <br>
    </div>
</template>

<script>
import { postForm,post } from "@/api";
export default {
    name: "goodsInfo",
    data() {
        return {
            editable: true,
            imageUrl: '',
            form: {
                name: '',
                tel: '',
                email: '',
                img: '',
                price: '',
                maker: '',
                picture: '',
                description: '',
                date: '',
                shelf_life: ''
            },
            ruleForm: {
                name: '',
                image: '',
                price: ''
            },
            rules: {
                name: [
                    { required: true, message: '请输入商品名称', trigger: 'blur' },
                ],
                image: [
                    { required: true, message: '请上传图片', trigger: 'blur' },
                ],
                price: [
                    { required: true, message: '请输入商品价格', trigger: 'blur' },
                ],
            }
        }
    },
    methods: {
        submitForm(formName) {
            let fd = new FormData()
            fd.append('name', formName.name)
            fd.append('price', formName.price)
            fd.append('picture', this.ruleForm.image)
            fd.append('seller_id', localStorage.getItem('userId'))
            console.log(typeof this.ruleForm.image)
            postForm(`http://43.143.179.158:8080/addGoods`, fd).then(res => {
                console.log(res)
            })
            .catch(function (error) {
                console.log(error);
            });
        },
        getImageFile: function (e) {
            let file = e.target.files[0];
            this.ruleForm.image = file;
            console.log(typeof file)
        },
        resetForm(formName) {
            this.$refs[formName].resetFields();
            this.ruleForm.image = '';
        },
    }
}
</script>

<style scoped>
.avatar {
    width: 100px;
    height: 100px;
}

.el-upload {
    width: 100px;
    height: 100px;
    line-height: 100px;
    margin-left: 60px;
}
</style>
