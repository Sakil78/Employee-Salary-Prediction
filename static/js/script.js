// Form submission handler
document.getElementById('predictionForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Show loading state
    const submitBtn = document.querySelector('.btn-predict');
    const originalText = submitBtn.innerHTML;
    submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Predicting...';
    submitBtn.disabled = true;
    
    const formData = new FormData(this);
    
    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            document.getElementById('monthly-salary').textContent = data.formatted_monthly;
            document.getElementById('annual-salary').textContent = data.formatted_annual;
            document.getElementById('result').style.display = 'block';
            
            // Smooth scroll to result
            document.getElementById('result').scrollIntoView({ 
                behavior: 'smooth' 
            });
        } else {
            alert('❌ Error: ' + data.error);
        }
    })
    .catch(error => {
        alert('❌ Error: ' + error);
    })
    .finally(() => {
        // Reset button state
        submitBtn.innerHTML = originalText;
        submitBtn.disabled = false;
    });
});

// Auto-select experience level based on years of experience
document.getElementById('experience').addEventListener('input', function() {
    const yearsOfExperience = parseInt(this.value);
    const experienceLevelSelect = document.getElementById('experience_level');
    
    if (isNaN(yearsOfExperience) || yearsOfExperience < 0) {
        experienceLevelSelect.value = '';
        experienceLevelSelect.classList.remove('auto-populated');
        return;
    }
    
    let selectedLevel = '';
    if (yearsOfExperience <= 1) {
        selectedLevel = 'Entry Level (0-1 years)';
    } else if (yearsOfExperience <= 3) {
        selectedLevel = 'Junior (2-3 years)';
    } else if (yearsOfExperience <= 7) {
        selectedLevel = 'Mid-Level (4-7 years)';
    } else if (yearsOfExperience <= 12) {
        selectedLevel = 'Senior (8-12 years)';
    } else if (yearsOfExperience <= 20) {
        selectedLevel = 'Lead/Principal (13-20 years)';
    } else {
        selectedLevel = 'Executive (>20 years)';
    }
    
    experienceLevelSelect.value = selectedLevel;
    experienceLevelSelect.classList.add('auto-populated');
});

// Allow manual override of auto-populated experience level
document.getElementById('experience_level').addEventListener('change', function() {
    if (this.value && !this.classList.contains('auto-populated')) {
        // User manually changed it, so don't auto-update anymore
        this.setAttribute('data-manual-override', 'true');
    }
});
