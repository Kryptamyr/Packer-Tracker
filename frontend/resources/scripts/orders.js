document.addEventListener('DOMContentLoaded', function() {
    const orderSearch = document.getElementById('order-search');
    const packerFilter = document.getElementById('packer-filter');
    const dateStart = document.getElementById('date-start');
    const dateEnd = document.getElementById('date-end');
    const clearFilters = document.getElementById('clear-filters');
    const ordersTable = document.getElementById('orders-table');
    const resultsCount = document.getElementById('results-count');
    
    // Get all table rows (excluding header)
    const tableRows = ordersTable ? Array.from(ordersTable.querySelectorAll('tbody tr')) : [];
    
    function filterOrders() {
        const searchTerm = orderSearch.value.toLowerCase();
        const selectedPacker = packerFilter.value;
        const startDate = dateStart.value;
        const endDate = dateEnd.value;
        
        let visibleCount = 0;
        
        tableRows.forEach(row => {
            const packerName = row.getAttribute('data-packer').toLowerCase();
            const orderNumber = row.getAttribute('data-order').toLowerCase();
            const orderDate = row.getAttribute('data-date');
            
            // Check search term
            const matchesSearch = !searchTerm || orderNumber.includes(searchTerm);
            
            // Check packer filter
            const matchesPacker = !selectedPacker || packerName === selectedPacker.toLowerCase();
            
            // Check date range
            let matchesDate = true;
            if (startDate && orderDate < startDate) {
                matchesDate = false;
            }
            if (endDate && orderDate > endDate) {
                matchesDate = false;
            }
            
            // Show/hide row based on all filters
            if (matchesSearch && matchesPacker && matchesDate) {
                row.style.display = '';
                visibleCount++;
            } else {
                row.style.display = 'none';
            }
        });
        
        // Update results count
        if (resultsCount) {
            resultsCount.textContent = `Showing ${visibleCount} orders`;
        }
    }
    
    // Add event listeners
    if (orderSearch) orderSearch.addEventListener('input', filterOrders);
    if (packerFilter) packerFilter.addEventListener('change', filterOrders);
    if (dateStart) dateStart.addEventListener('change', filterOrders);
    if (dateEnd) dateEnd.addEventListener('change', filterOrders);
    
    // Clear filters
    if (clearFilters) {
        clearFilters.addEventListener('click', function() {
            if (orderSearch) orderSearch.value = '';
            if (packerFilter) packerFilter.value = '';
            if (dateStart) dateStart.value = '';
            if (dateEnd) dateEnd.value = '';
            filterOrders();
        });
    }
    
    // Initialize filter
    filterOrders();
}); 