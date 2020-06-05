import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Cover from '@/components/HOME/Cover'
import Login from '@/components/Login'
import Home from '@/components/Home'
import LibraryIndex from '@/components/library/LibraryIndex'
import UserIndex from '@/components/User/UserIndex'
import PresentationIndex from '@/components/Presentation/PresentationIndex'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/home',
      name: 'Home',
      component: Home,
      // home页面并不需要被访问
      redirect: '/index',
      children: [
        {
          path: '/index',
          name: 'Cover',
          component: Cover,
          meta: {
            requireAuth: false
          }
        },
        {
          path: '/parameter',
          name: 'Library',
          component: LibraryIndex,
          meta: {
            requireAuth: true
          }
        },
        {
          path: '/presentation',
          name: 'Presentation',
          component: PresentationIndex,
          meta: {
            requireAuth: true
          }
        },
        {
          path: '/admin',
          name: 'User',
          component: UserIndex,
          meta: {
            requireAuth: true
          }
        }
      ]
    }
  ]
})
