<script>
export default{
    props: {
        questionnaire : Object
    }
}
</script>
<template>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
      <div v-bind:class="{questionnaire}">
        <p v-bind="questionnaire"> {{ questionnaire.name }}</p>
      </div>
</template>