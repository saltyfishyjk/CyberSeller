// appfront/src/api/api.js
import axios from "axios"

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
        "Content-Type": 'multipart/form-data'
    };
    return new Promise((resolve, reject) => {
        axios
            .post(url, json ? JSON.stringify(params) : params, {
                headers: json ? headerJSON : headerFormData,
                responseType: "json"
            })
            .then(res => {
                resolve(res.data);
            })
            .catch(err => {
                reject(err.data);
            });
    });
}

export const userLogin = async (para) => {
    await post(`http://43.143.179.158:8080/login`, {
        "name": para.username,
        "password": para.password
    }, true).then(res => {
        console.log(res)
        if (res.succeed) {
            localStorage.setItem('username', para.username);
            localStorage.setItem('userId', res.id);
        } else {
            localStorage.setItem('username', 'admin');
        }
    })
    .catch(function (error) {
        console.log(error);
    });
}

export const userSignUp = async (para) => {
    await post(`http://43.143.179.158:8080/signup`, {
        "name": para.username,
        "password": para.password,
        "identity": "customer"
    }, true).then(res => {
        console.log(res)
        if (res.succeed) {
            localStorage.setItem('username', para.username);
            localStorage.setItem('userId', res.id);
        } else {
            localStorage.setItem('username', 'admin');
        }
    })
        .catch(function (error) {
            console.log(error);
        });
}

export const addGoods = async (para) => {
    console.log(para.get('name'))
    await post(`http://43.143.179.158:8080/addGoods`, para, false).then(res => {
        console.log(res)
    })
        .catch(function (error) {
            console.log(error);
        });
}

export function postForm(url, data = {}) {
    return new Promise((resolve, reject) => {
        axios.create({
            withCredentials: true,
            headers: {  'Content-Type': "multipart/form-data" },
        }).post(url, data).then(response => {
            resolve(response.data)
        }, err => {
            reject(err)
        })
    })
}


export const mainRecommendGoods = async () => {
    let fd = new FormData()
    fd.append('user_id', localStorage.getItem('userId'))
    console.log('user_id' + localStorage.getItem('userId'))
    postForm(`http://43.143.179.158:8080/mainRecommendGoods`, fd).then(res => {
        console.log(res)
        return Promise.resolve(res.goods)
    })
    .catch(function (error) {
        console.log(error);
    });
}