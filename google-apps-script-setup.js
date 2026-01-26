/**
 * Sharp Money Collective - Auto Setup Script
 * Run this once in your Google Sheet to create all tabs
 *
 * HOW TO USE:
 * 1. Open your Google Sheet
 * 2. Go to Extensions → Apps Script
 * 3. Delete any existing code
 * 4. Paste this entire script
 * 5. Click Save (disk icon)
 * 6. Click Run (play icon) → Select "setupSharpMoneyCollective"
 * 7. Authorize when prompted
 * 8. Wait 10 seconds - Done!
 */

function setupSharpMoneyCollective() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();

  // Delete old tabs if they exist
  ['Meta', 'Stats', 'Positions', 'Events', 'Scenarios'].forEach(name => {
    const sheet = ss.getSheetByName(name);
    if (sheet) ss.deleteSheet(sheet);
  });

  Logger.log('Creating Sharp Money Collective tabs...');

  // Create Meta tab
  createMetaTab(ss);

  // Create Stats tab
  createStatsTab(ss);

  // Create Positions tab
  createPositionsTab(ss);

  // Create Events tab
  createEventsTab(ss);

  // Create Scenarios tab
  createScenariosTab(ss);

  SpreadsheetApp.getUi().alert('✅ Sharp Money Collective tabs created!\n\nYour portfolio dashboard is ready. Refresh your website to see it live.');
  Logger.log('✅ Setup complete!');
}

function createMetaTab(ss) {
  const sheet = ss.insertSheet('Meta');

  // Headers
  sheet.getRange('A1:B1').setValues([['Field', 'Value']]);
  sheet.getRange('A1:B1').setFontWeight('bold').setBackground('#667eea').setFontColor('#ffffff');

  // Data
  const data = [
    ['Last Updated', new Date().toLocaleString('en-US', { timeZone: 'America/Los_Angeles' })],
    ['Day', 1],
    ['Challenge Start', '2026-01-25'],
    ['Challenge End', '2026-02-24']
  ];

  sheet.getRange(2, 1, data.length, 2).setValues(data);
  sheet.setColumnWidth(1, 200);
  sheet.setColumnWidth(2, 300);

  Logger.log('✓ Meta tab created');
}

function createStatsTab(ss) {
  const sheet = ss.insertSheet('Stats');

  // Headers
  sheet.getRange('A1:B1').setValues([['Metric', 'Value']]);
  sheet.getRange('A1:B1').setFontWeight('bold').setBackground('#667eea').setFontColor('#ffffff');

  // Data
  const data = [
    ['Working Capital Total', 119.00],
    ['Working Capital Available', 19.00],
    ['Working Capital Pending', 100.00],
    ['Starting Bankroll', 140.00],
    ['Current Value', 140.00],
    ['Total Return', 0.00],
    ['Total Return %', 0.00],
    ['Active Bets', 4],
    ['Settled Bets', 0],
    ['Win Rate', '-'],
    ['Deployment Rate', 0.16]
  ];

  sheet.getRange(2, 1, data.length, 2).setValues(data);
  sheet.setColumnWidth(1, 250);
  sheet.setColumnWidth(2, 150);

  // Format currency cells
  sheet.getRange('B2:B7').setNumberFormat('$#,##0.00');

  Logger.log('✓ Stats tab created');
}

function createPositionsTab(ss) {
  const sheet = ss.insertSheet('Positions');

  // Headers
  const headers = [
    'ID', 'Title', 'Type', 'Platform', 'Position', 'Amount',
    'Entry Price', 'Contracts', 'Potential Profit', 'Profit %',
    'Settlement', 'Est Prob', 'Market Prob', 'Risk', 'Reasoning'
  ];

  sheet.getRange(1, 1, 1, headers.length).setValues([headers]);
  sheet.getRange(1, 1, 1, headers.length).setFontWeight('bold').setBackground('#667eea').setFontColor('#ffffff');

  // Data
  const data = [
    [
      'unemployment-jan26',
      'January 2026 Unemployment Rate >4.5%',
      'short',
      'Kalshi',
      'YES',
      10.00,
      0.20,
      50,
      40.00,
      400,
      '2026-02-06',
      0.375,
      0.20,
      'low',
      'Economist consensus forecasts 4.5%, market only pricing 20% chance. My estimate: 35-40% true probability.'
    ],
    [
      'payrolls-jan26',
      'January 2026 Nonfarm Payrolls ≤70k',
      'short',
      'Kalshi',
      'NO on >70k',
      10.00,
      0.41,
      24.4,
      14.40,
      144,
      '2026-02-06',
      0.75,
      0.41,
      'low',
      'JPMorgan forecasts only 25k/month Q1, market overpricing upside. My estimate: 75-80% true probability for ≤70k.'
    ],
    [
      'openai-ipo',
      'OpenAI IPO Before Jun 1 2027',
      'long',
      'Kalshi',
      'YES',
      50.00,
      0.61,
      82,
      32.00,
      64,
      '2027-06-01',
      '-',
      0.61,
      'high',
      'Speculative bet on OpenAI IPO timing. 17-month timeline with significant uncertainty.'
    ],
    [
      'jony-ive',
      'Jony Ive Device: Clip-on',
      'long',
      'Kalshi',
      'Clip-on',
      50.00,
      0.42,
      119,
      69.00,
      138,
      'TBD',
      '-',
      0.42,
      'very-high',
      'Pure speculation on product form factor. Very high risk of insider information advantages.'
    ]
  ];

  sheet.getRange(2, 1, data.length, headers.length).setValues(data);

  // Auto-resize columns
  for (let i = 1; i <= headers.length; i++) {
    sheet.autoResizeColumn(i);
  }

  // Make reasoning column wider
  sheet.setColumnWidth(15, 400);

  // Format currency and number columns
  sheet.getRange(2, 6, data.length, 1).setNumberFormat('$#,##0.00'); // Amount
  sheet.getRange(2, 7, data.length, 1).setNumberFormat('$0.00'); // Entry Price
  sheet.getRange(2, 9, data.length, 1).setNumberFormat('$#,##0.00'); // Potential Profit

  Logger.log('✓ Positions tab created');
}

function createEventsTab(ss) {
  const sheet = ss.insertSheet('Events');

  // Headers
  sheet.getRange('A1:C1').setValues([['Date', 'Time', 'Description']]);
  sheet.getRange('A1:C1').setFontWeight('bold').setBackground('#667eea').setFontColor('#ffffff');

  // Data
  const data = [
    ['Next Week', '-', '+$100 capital deposit arrives • Deploy 20-30% into new positions'],
    ['2026-02-06', '8:30 AM ET', 'BLS Jobs Report → Unemployment & Payrolls bets settle • Max profit: +$54.40'],
    ['2026-02-11', '-', 'CPI Inflation Data Release • Potential new opportunities'],
    ['2026-02-24', '-', 'Challenge Period Ends • Performance Review']
  ];

  sheet.getRange(2, 1, data.length, 3).setValues(data);
  sheet.setColumnWidth(1, 150);
  sheet.setColumnWidth(2, 100);
  sheet.setColumnWidth(3, 500);

  Logger.log('✓ Events tab created');
}

function createScenariosTab(ss) {
  const sheet = ss.insertSheet('Scenarios');

  // Headers
  sheet.getRange('A1:E1').setValues([['Name', 'Emoji', 'Total Profit', 'Final Bankroll', 'Return %']]);
  sheet.getRange('A1:E1').setFontWeight('bold').setBackground('#667eea').setFontColor('#ffffff');

  // Data
  const data = [
    ['Best Case (All Win)', '🎯', 155.40, 295.40, 111],
    ['Short-Term Only (Feb 6)', '📊', 54.40, 194.40, 39],
    ['Worst Case (All Lose)', '⚠️', -121.00, 19.00, -86]
  ];

  sheet.getRange(2, 1, data.length, 5).setValues(data);
  sheet.setColumnWidth(1, 250);
  sheet.setColumnWidth(2, 80);
  sheet.setColumnWidth(3, 150);
  sheet.setColumnWidth(4, 150);
  sheet.setColumnWidth(5, 100);

  // Format currency columns
  sheet.getRange(2, 3, data.length, 2).setNumberFormat('$#,##0.00');

  Logger.log('✓ Scenarios tab created');
}

/**
 * Auto-update timestamp (optional - run this daily)
 */
function updateTimestamp() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const metaSheet = ss.getSheetByName('Meta');

  if (metaSheet) {
    metaSheet.getRange('B2').setValue(new Date().toLocaleString('en-US', { timeZone: 'America/Los_Angeles' }));
    Logger.log('✓ Timestamp updated');
  }
}

/**
 * Increment day counter (optional - run this daily)
 */
function incrementDay() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const metaSheet = ss.getSheetByName('Meta');

  if (metaSheet) {
    const currentDay = metaSheet.getRange('B3').getValue();
    metaSheet.getRange('B3').setValue(currentDay + 1);
    Logger.log('✓ Day incremented to ' + (currentDay + 1));
  }
}
