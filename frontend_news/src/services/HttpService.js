import Cookie from 'js-cookie';

const HttpService = {
  req_headers: {
    'Authorization': Cookie.get('user_id')
  },
  get_news(type){
    const req_info = {
      method: 'GET',
      headers: this.req_headers
    }
    return fetch(`${process.env.REACT_APP_HOSTURL}/get_news/?type=${type}`, req_info)
      .then(res => res.json())
  }
}

export default HttpService;