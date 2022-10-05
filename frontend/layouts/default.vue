<template>
  <v-app dark>
    <v-main>
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>
    <v-footer
      absolute
      app
    >
      <span>Project &copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>
