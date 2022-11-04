node("slave") {
    stage('Results') {
        echo "Hello pipe part 2"
        sh 'ip l'
    }
}
