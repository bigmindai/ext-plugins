# Revenue Analytics Boundaries

Check capability before calculating. The Bigmind connector is strong for bounded CRM and conversation review but does not expose a general analytics warehouse.

## Supported With Available Records

- opportunity counts and amounts for returned opportunities;
- pipeline counts and total amount by stage from `getPipelineStageSummary`;
- risk summaries based on stored warnings and retrieved evidence;
- account, deal, meeting, activity, note, todo, signal, and authenticated-user email synthesis;
- tracker-backed meeting cohorts with pagination;
- simple calculations over a clearly bounded returned dataset.

## Potentially Incomplete or Unsupported

- exhaustive historical cohorts when opportunity results are truncated;
- stage-transition history and average days between stages;
- touches before opportunity creation or close without a complete attributed activity history;
- statistical correlation, predictive power, or causal claims;
- product-usage analysis unless usage is present in accessible signals or CRM fields;
- arbitrary teammate mailbox analysis;
- webinar registration and attendance analytics;
- authoritative Salesforce implementation output when required fields or history are unavailable.

## Respond Safely

When a requested metric cannot be established:

1. compute only what the returned data supports;
2. label the result as bounded or exploratory;
3. list the missing data or connector capability;
4. avoid substituting qualitative impressions for the requested metric;
5. propose the smallest additional data source or MCP tool needed.

Never convert missing values to zero unless zero is explicitly represented in the source.
