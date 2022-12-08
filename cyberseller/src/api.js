// appfront/src/api/api.js
import axios from "axios"
var user = {
    name: "123@qq.com",
    password: "123",
    identity: "customer"
}

axios.interceptors.response.use(response => { //axios拦截器

    if (response.status === 200) { //响应成功后

        if (response.headers['message']) {
            console.log(response.headers['message'])

        }
        return Promise.resolve(response);

    } else {

        return Promise.reject(response);

    }
})
var params = new URLSearchParams();
params.append('key', 'value');
export function post(url, params = {}, json = false) {
    // json格式请求头
    const headerJSON = {
        "Content-Type": "application/json"
    };
    // FormData格式请求头
    const headerFormData = {
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
    };
    return new Promise((resolve, reject) => {
        axios
            .post(url, json ? JSON.stringify(params) : qs.stringify(params), {
                headers: json ? headerJSON : headerFormData,
            responseType:"json"})
            .then(res => {
                console.log(res['message']);
                resolve(res.data);
            })
            .catch(err => {
                reject(err.data);
            });
    });
}

export const userLogin = async () => {
    await post(`http://43.143.179.158:8080/login`, {
        "name": "123@qq.com",
        "password": "123"
    }, true).then(res => {
        
        console.log(res['message']);
        console.log(res.message);
    })
        .catch(function (error) {
            console.log(error);
        }); }

export const userSignUp = async () => {
    let result = await post(`http://43.143.179.158:8080/signup`, {
        "name": "123@qq.com",
        "password": "123",
        "identity": "customer"
    }, true)
    console.log("result->"+result)
}

