node("slave") {
    stage('Results') {
        echo "Hello pipe part 1"
        sh 'ip l'
    }
}
