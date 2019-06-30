(function () {
    document.addEventListener('DOMContentLoaded', function () {
        const form = document.getElementById('checkout');
        const countInput = document.getElementById('checkout_count');
        const countDisplay = document.getElementById('checkout_count_display');
        const costDisplay = document.getElementById('checkout_cost_display');
        const calculateCost = (voteCount) => {
            voteCount = parseInt(voteCount, 10)
            if (voteCount >= 5) {
                return (voteCount * 0.7).toFixed(2);
            }
            return voteCount.toFixed(2);
        }
        const onCountUpdate = () => {
            const {value} = countInput
            countDisplay.innerText = value;
            costDisplay.innerText = calculateCost(value)
        };

        document.querySelectorAll(".purchase_button").forEach(function (element) {
            element.addEventListener('click', function (event) {
                console.log(event.target.dataset.count)
                const {count} = event.target.dataset;

                countInput.value = count;
                onCountUpdate();
            });
        });

        countInput.addEventListener("change", onCountUpdate);

        onCountUpdate();
    });

})()