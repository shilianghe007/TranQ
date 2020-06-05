import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: {
      username: window.localStorage.getItem('user' || '[]') == null ? '' : JSON.parse(window.localStorage.getItem('user' || '[]')).username
    },
    location: window.localStorage.getItem('location') == null ? '' : JSON.parse(window.localStorage.getItem('location')),
    car: window.localStorage.getItem('car') == null ? '' : JSON.parse(window.localStorage.getItem('car')),
    token: window.localStorage.getItem('token') == null ? '' : JSON.parse(window.localStorage.getItem('token')),
    cityNumber: window.localStorage.getItem('cityNumber') == null ? '' : window.localStorage.getItem('cityNumber'),
    lengths: '',
    iterNum: window.localStorage.getItem('iterNum') == null ? '' : window.localStorage.getItem('iterNum')
  },
  mutations: {
    login (state, user) {
      state.user = user
      window.localStorage.setItem('user', JSON.stringify(user))
    },
    setLocs (state, locs) {
      state.location = locs
      window.localStorage.setItem('location', JSON.stringify(locs))
    },
    setCars (state, cars) {
      state.car = cars
      window.localStorage.setItem('car', JSON.stringify(cars))
    },
    setToken (state, token) {
      state.token = token
      window.localStorage.setItem('token', JSON.stringify(token))
    },
    setCityNum (state, cityNumber) {
      state.cityNumber = cityNumber
      window.localStorage.setItem('cityNumber', JSON.stringify(cityNumber))
    },
    setLength (state, lengths) {
      state.lengths = lengths
    },
    setIterNum (state, iterNum) {
      state.iterNum = iterNum
      window.localStorage.setItem('iterNum', JSON.stringify(iterNum))
    }
  }
})
